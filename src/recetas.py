from typing import NamedTuple,List, Tuple
import csv
from datetime import date,datetime

Ingrediente = NamedTuple("Ingrediente",
					     [("nombre",str),
						  ("cantidad",float),
						  ("unidad_medida",str)])
						 
Receta = NamedTuple("Receta", 
                    [("denominacion", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", list[Ingrediente]),
                     ("tiempo", int),
                     ("calorias", int),
                     ("fecha", date),
                     ("precio", float)])

def lee_recetas(ruta:str)-> List[Receta]:
    recetas = []
    with open(ruta,encoding = 'utf8') as f:
        lector = csv.reader(f,delimiter=';')
        next(lector)
        for linea in lector:
            denominacion = linea[0].strip()
            tipo = linea[1].strip()
            dificultad = linea[2].strip()
            ingredientes = parsea_ingredientes(linea[3].strip())
            tiempo = int(linea[4].strip())
            calorias = int(linea[5].strip())
            fecha = datetime.strptime(linea[6].strip(),"%d/%m/%Y").date()
            precio = float(linea[7].strip().replace(',','.')) #cuidado que en el csv vienen los precios 8,99 en vez de 8.99
            recetas.append(Receta(denominacion,tipo,dificultad,ingredientes,tiempo,calorias,fecha,precio))
    return recetas

def parsea_ingredientes(i:str)->list[Ingrediente]:
    res = []
    i = i.strip()
    if len(i)>0:
        ingredientes = i.split(',')
        for ig in ingredientes:
            res.append(parsea_ingrediente(ig))
    return res



def parsea_ingrediente(i:str)->Ingrediente:
    
    nombre,cantidad,unidades = i.split('-')
    nombre = nombre.strip()
    cantidad = float(cantidad.strip())
    unidades = unidades.strip()
    return Ingrediente(nombre,cantidad,unidades)


def ingredientes_en_unidad_medida(r:List[Receta],u:str|None =None)->int:

   l = {b.nombre for a in r for b in a.ingredientes if b.unidad_medida == u or b.unidad_medida is None }
   return len(l)

def recetas_con_ingredientes(r:List[Receta],con:set[str])->List[Tuple[str,int,float]]:
    l = [(a.denominacion,a.calorias,a.precio) for a in r if any(b.nombre in con for b in a.ingredientes) ] 
    #el any es como un or que sirve para agregar la receta si uno de los ingredientes esta en el con, asi no se repiten recetas
    # si se cumple cualquiera de esto , list.append((a.den...))
    return l


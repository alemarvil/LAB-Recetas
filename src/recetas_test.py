from recetas import *



if __name__ == "__main__":
    a = lee_recetas('data/recetas.csv')
    b = ingredientes_en_unidad_medida(a,'gr')
    c = recetas_con_ingredientes(a,'tomate frito, pasta')
    d = receta_mas_barata(a,{'Plato principal'},4)
    e = recetas_baratas_con_menos_calorias(a,6)
    print(e)

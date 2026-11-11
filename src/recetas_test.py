from recetas import *



if __name__ == "__main__":
    a = lee_recetas('data/recetas.csv')
    b = ingredientes_en_unidad_medida(a,'gr')
    c = recetas_con_ingredientes(a,'tomate frito, pasta')
    print(c)

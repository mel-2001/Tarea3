import statistics

def calculos(lista1, lista2):
    listaFinal = lista1 + lista2
    listaFinal.sort()
    print("Lista ordenada: ")
    print(listaFinal)
    print("-----------------------------")
    media = statistics.mean(listaFinal)
    print("Media: ")
    print(media)
    print("-----------------------------")
    desviacion = statistics.pstdev(listaFinal)
    print("Desviacion estandar: ")
    print(desviacion)
    print("-----------------------------")
    mediana = statistics.median(listaFinal)
    print("Mediana:")
    print(mediana)
    print("-----------------------------")
    print(lista1)
    eliminarPares(lista1)
    print(lista1)

def eliminarPares(lista1):
    for i in lista1[:]:
        if (i % 2 == 0):
            lista1.remove(i)

calculos( [13,2,104,45,36,9,120,29,2,500,89,4165 ], [203,30,190,47,22,77,0,177,110,313,15,23])
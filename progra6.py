#Estrategia divide y vencerás

def quicksort(lista):
    quicksort2(lista, 0, len(lista)-1)

def quicksort2(lista, inicio, fin):
    if inicio < fin:
        pivote = particion(lista, inicio, fin)
        quicksort2(lista, inicio, pivote-1)
        quicksort2(lista, pivote+1, fin)

def particion(lista, inicio, fin):
    pivote = lista[inicio]
    izquierda = inicio+1 
    derecha = fin
    bandera = False
    while not bandera:
        while izquierda<= derecha and lista[izquierda] <= pivote:
            izquierda = izquierda+1
        while derecha >= izquierda and lista[derecha] >= pivote:
            derecha = derecha -1
        if derecha < izquierda:
            bandera = True
        else:
            temp = lista[izquierda]
            lista[izquierda] = lista[derecha]
            lista[derecha] = temp
    temp = lista[inicio]
    lista[inicio] = lista[derecha]
    lista[derecha] = temp
    return derecha

lista = [21, 10, 0, 11, 0, 24, 14, 1]
quicksort(lista)
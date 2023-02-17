a=[-1,20,6,5,4,3,2,1]


def existe_en_arreglo_recursivo(arreglo, numero, indice=0):
    if indice == len(arreglo):
        return False
    if arreglo[indice] == numero:
        return True
    return existe_en_arreglo_recursivo(arreglo, numero, indice + 1)

print(existe_en_arreglo_recursivo(a,21))
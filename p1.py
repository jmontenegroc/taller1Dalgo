def suma_diagonal(matriz):
    n = len(matriz)
    suma = 0
    for i in range(n):
        suma += matriz[i][i]
    return suma


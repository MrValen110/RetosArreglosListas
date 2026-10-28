def invertir_arreglo(arreglo):
    inicio = 0
    fin = len(arreglo) - 1

    while inicio < fin:
        temporal = arreglo[inicio]
        arreglo[inicio] = arreglo[fin]
        arreglo[fin] = temporal

        inicio += 1
        fin -= 1

    return arreglo


numeros = [1, 2, 3, 4, 5]

invertir_arreglo(numeros)

print(numeros)  # [5, 4, 3, 2, 1]
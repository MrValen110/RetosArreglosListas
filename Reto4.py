def mover_ceros(arreglo):
    indice_no_cero = 0

    for i in range(len(arreglo)):
        if arreglo[i] != 0:
            arreglo[indice_no_cero] = arreglo[i]
            indice_no_cero += 1

    for i in range(indice_no_cero, len(arreglo)):
        arreglo[i] = 0

    return arreglo


numeros = [0, 1, 0, 3, 12]

mover_ceros(numeros)

print(numeros)  # [1, 3, 12, 0, 0]
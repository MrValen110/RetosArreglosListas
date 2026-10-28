def buscar_indice(arreglo, valor):
    for i in range(len(arreglo)):
        if arreglo[i] == valor:
            return i

    return -1


numeros = [10, 20, 30, 40, 50]

print(buscar_indice(numeros, 30))  # 2
print(buscar_indice(numeros, 99))  # -1
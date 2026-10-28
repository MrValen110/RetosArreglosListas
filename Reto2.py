def sumar_elementos(arreglo):
    suma = 0

    for i in range(len(arreglo)):
        suma += arreglo[i]

    return suma


numeros = [5, 10, 15, 20]

print(sumar_elementos(numeros))  # 50
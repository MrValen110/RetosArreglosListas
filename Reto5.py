def encontrar_faltante(arreglo, n):
    suma_ideal = n * (n + 1) // 2
    suma_real = 0

    for i in range(len(arreglo)):
        suma_real += arreglo[i]

    return suma_ideal - suma_real


numeros = [1, 2, 4, 5, 6]

print(encontrar_faltante(numeros, 6))  # 3
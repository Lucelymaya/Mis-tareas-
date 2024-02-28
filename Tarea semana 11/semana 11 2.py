def ordenar_fila(matriz, nu_fila):
    # Verificar si la fila está dentro del rango válido
    if 0 <= nu_fila < len(matriz):
        # Ordenar la fila usando el algoritmo de ordenación (Bubble Sort en este caso)
        matriz[nu_fila] = bubble_sort(matriz[nu_fila])

def bubble_sort(fila):
    n = len(fila)

    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

    return fila

# Definir una matriz de ejemplo 3x3
matriz_e = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]
#Muestra la matriz original
print("Matriz original:")
for fila in matriz_e:
    print(fila)

#ordena la fila 1 en orden acendete
fila_a_ordenar = 1
ordenar_fila(matriz_e, fila_a_ordenar)
#muetra la matriz ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_e:
    print(fila)
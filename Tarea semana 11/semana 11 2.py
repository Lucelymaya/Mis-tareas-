def ordenar_fila(matriz, fila):
    fila_ordenada = sorted(matriz[fila])
    matriz[fila] = fila_ordenada

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    matriz = [
        [3, 1, 4],
        [1, 5, 9],
        [2, 6, 5]
    ]

    fila_a_ordenar = 1

    print("Matriz original:")
    imprimir_matriz(matriz)

    ordenar_fila(matriz, fila_a_ordenar)

    print("\nMatriz con la fila ordenada:")
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()

# Definir la matriz
matriz = [
    [9, 7, 6],
    [3, 2, 1],
    [5, 8, 4]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegir la fila a ordenar (en este caso, la fila 1)
fila_a_ordenar = 1

# Ordenar la fila seleccionada (utilizando Bubble Sort)
n = len(matriz[0])
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if matriz[fila_a_ordenar][j] > matriz[fila_a_ordenar][j + 1]:
            matriz[fila_a_ordenar][j], matriz[fila_a_ordenar][j + 1] = matriz[fila_a_ordenar][j + 1], matriz[fila_a_ordenar][j]

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)

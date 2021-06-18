import numpy as np

matriz1, matriz2 = [], []

print(matriz1, matriz2)

print("Ingrese dimensiones de la matriz1")

row1 = int(input("Numero de filas "))
col1 = int(input("Numero de columnas "))

print("Ingrese dimensiones de la matriz2")

row2 = int(input("Numero de filas "))
col2 = int(input("Numero de columnas "))


if(col1 != row2):

    print('Valores no validos para multiplicación')
else:
    print('Complete la matriz1')
    for i in range(row1):
        array1 = []
        for j in range(col1):
            array1.append(
                int(input("Ingrese el valor en la posición (%d,%d) " % (i, j))))

        matriz1.append(array1)

    print("Matriz 1")
    for i in range(row1):

        print(matriz1[i])

    a = np.array(matriz1)

    print('Complete la matriz2')
    for i in range(row2):
        array2 = []
        for j in range(col2):
            array2.append(
                int(input("Ingrese el valor en la posición (%d,%d) " % (i, j))))

        matriz2.append(array2)

    print("Matriz 2")
    for k in range(row2):

        print(matriz2[k])

    b = np.array(matriz2)

    c = np.dot(a, b)

    print("Matriz resultante")
    print(c)

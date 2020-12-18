from menus import *
# Función Ingresar Matrices
def IngresarMatrices(lmatrices, indiceM, guardar=False, new_matriz=0):
    memoria = open('memoria.txt', 'w')
    while True:
        indice = 0
        if (opcion := MenuIngresarMatrices()) == '1':
            while True:
                print('¿Esta segur@ que desea reemplazar una memoria existente?\n[1]Si\n[2]No')
                confirmacion = input("Reemplazar matriz - Seleccionar opción: ")
                if confirmacion == '1':
                    for i, matriz in enumerate(lmatrices[indiceM]):
                        print(f'Matriz {i + 1}: {len(matriz)}x{len(matriz[0])}')
                    while not(indice := int(input("Reemplazar matriz - Ingrese índice: ")) in [i for i in range(1, len(lmatrices[indiceM])+1)]):
                        print('Indice Inexistente. Intente nuevamente')
                    lmatrices[indiceM].remove(lmatrices[indiceM][indice-1])
                    memoria.write(str(lmatrices))
                    break
                elif confirmacion == '2':
                    break
                print('Opción Inexistente. Intente nuevamente')
        if opcion in '12' and not guardar:
            new_matriz = [[int(j) for j in input(f"Ingresar Matriz - Elementos de fila {i + 1}: ").split(",")]
                          for i in range(int(input("Ingresar Matriz - Número de filas: ")))]
            for f in new_matriz:
                if len(new_matriz[0]) != len(f):
                    print("¡Vaya! parece que el numero de columnas no coincide porfavor inserte una matriz valida")
                    new_matriz = None
            if new_matriz:
                lmatrices[indiceM].append(new_matriz) if opcion == '2' else lmatrices[indiceM].insert(indice-1, new_matriz)
                memoria.write(str(lmatrices))
                print("La matriz se guardo exitosamente ")
        else:
            if guardar:
                lmatrices.append(new_matriz) if opcion == '2' else lmatrices.insert(indice - 1, new_matriz)
                memoria.write(str(lmatrices))
                print("La matriz se guardó exitosamente ")
                break
            if opcion == '3':
                break
            print('Opción Inexistente. Intente nuevamente')

# Función Operar Matrices
def OperarMatrices(lmatrices, indiceM):
    if not (lmatrices[indiceM] == []):
        if (operacion := MenuOperarMatrices()) != '5':
            while True:
                for i, matriz in enumerate(lmatrices[indiceM]):
                    print(f'Matriz {i + 1}: {len(matriz)}x{len(matriz[0])}')
                indices = [i for i in range(len(lmatrices[indiceM]))]
                while not ((indice1 := int(input("Operar matriz - Ingrese índice 1: "))-1) in indices):
                    print('Indice Inexistente. Intente nuevamente')
                indice2 = indice1
                if operacion != '4':
                    while not ((indice2 := int(input("Operar matriz - Ingrese índice 2: "))-1) in indices):
                        print('Indice Inexistente. Intente nuevamente')
                if len(matriz1 := lmatrices[indiceM][indice1]) == len(matriz2 := lmatrices[indiceM][indice2]):
                    matriz_res = []
                    if operacion == '1':
                        matriz_res = [[matriz1[f][c]+matriz2[f][c] for c in range(len(matriz1))] for f in range(len(matriz1))]
                    elif operacion == '2':
                        matriz_res = [[matriz1[f][c]-matriz2[f][c] for c in range(len(matriz1))] for f in range(len(matriz1))]
                    elif operacion == '3':
                        temp = 0
                        for f in range(len(matriz1)):
                            for c in range(len(matriz1)):
                                for i in range(len(matriz1)):
                                    temp += matriz1[f][i] * matriz2[i][c]
                                matriz_res[f][c] = temp
                    elif operacion == '4':
                        matriz_res = [[matriz1[c][f] for c in range(len(matriz1))] for f in range(len(matriz1))]
                    if not (matriz_res == []):
                        print("Las matrices se operaron exitosamente ")
                        for f, fila in enumerate(matriz_res):
                            for c, columna in enumerate(fila):
                                print(' ', matriz_res[f][c], end='')
                            print()
                        IngresarMatrices(lmatrices, indiceM, True, matriz_res)
                else:
                    print("¡Vaya! parece que las dimensiones de ambas matrices no coincide. Seleccione dos matrices válidas")
    else:
        print("¡Vaya! parece que aún no hay matrices guardadas. Ingrese 2 o más matrices")
        IngresarMatrices(lmatrices, indiceM)

# Función Mostrar Matrices
def MostrarMatrices(lmatrices, indiceM):
    if not (lmatrices[indiceM] == []):
        while True:
            if (opcion := MenuMostrarMatrices()) in '12':
                for i, matriz in enumerate(lmatrices[indiceM]):
                    print(f'Matriz {i + 1}: {len(matriz)}x{len(matriz[0])}')
                if opcion == '2':
                    matriz = int(input('Ingrese numero de Matriz: ')) - 1
                    for f, fila in enumerate(lmatrices[indiceM][matriz]):
                        for c, columna in enumerate(fila):
                            print(' ', lmatrices[indiceM][matriz][f][c], end='')
                        print()
            else:
                if opcion == '3':
                    break
                print('Opción Inexistente. Intente nuevamente')
    else:
        print("¡Vaya! parece que aún no hay matrices guardadas. Ingrese una matriz")
        IngresarMatrices(lmatrices[indiceM])

# Función Finalizar
def Finalizar():
    import sys
    print('Proceso finalizado! Gracias')
    sys.exit()

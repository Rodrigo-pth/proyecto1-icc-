# Función Ingresar Matrices
def IngresarMatrices(lmatrices,indiceM):
    print('[1]Ingresar Matriz en una menoria existente\n[2]Ingresar Matriz a una memoria\n[3]Salir')
    while (opcion1 := input('Ingresar Matrices - Seleccionar opción: ')) in '12':
        indice = 0
        while opcion1 == '1':
            print('¿Esta segur@ que desea reemplazar una memoria existente?\n[1]Si\n[2]No')
            if (opcion2 := input("Reemplazar matriz - Seleccionar opción: ")) in '12':
                if opcion2 == '1':
                    for i, matriz in enumerate(lmatrices[indiceM]):
                        print(f'Matriz {i + 1}: {len(matriz)}x{len(matriz[0])}')
                    while not((indice := int(input("Reemplazar matriz - Ingrese índice: "))) in
                              [i for i in range(1, len(lmatrices)+1)]):
                        print('Indice Inexistente. Intente nuevamente')
                    lmatrices[indiceM].remove(lmatrices[indiceM][indice-1])
                elif opcion2 == '2':
                    IngresarMatrices(lmatrices,indiceM)
                break
            else:
                print('Opción Inexistente. Intente nuevamente')
        new_matriz = [[int(j) for j in input(f"Elementos de fila {i + 1}: ").split(",")]
                      for i in range(int(input("Reemplazar matriz - Número de filas: ")))]
        for f in new_matriz:
            if len(new_matriz[0]) != len(f):
                print("¡Vaya! parece que el numero de columnas no coincide porfavor inserte una matriz valida")
                new_matriz = None
                print('[1]Ingresar Matriz en una menoria existente\n[2]Ingresar Matriz a una memoria\n[3]Salir')
                break
        if new_matriz:
            lmatrices[indiceM].append(new_matriz) if opcion1 == '2' else lmatrices[indiceM].insert(indice - 1, new_matriz)
            print("La matriz se guardo exitosamente ")
            print('[1]Ingresar Matriz en una menoria existente\n[2]Ingresar Matriz a una memoria\n[3]Salir')
    else:
        if opcion1 != '3':
            print('Opción Inexistente. Intente nuevamente')
            IngresarMatrices(lmatrices,indiceM)

# Función Operar Matrices
def OperarMatrices(lmatrices,indiceM):
    if not (lmatrices[indiceM] == []):
        print('[1]Sumar\n[2]Restar\n[3]Multiplicar\n[4]Trasponer\n[5]Salir')
        while (opcion1 := input('Operar Matrices - Seleccionar opción: ')) in '1234':
            for i, matriz in enumerate(lmatrices[indiceM]):
                print(f'Matriz {i + 1}: {len(matriz)}x{len(matriz[0])}')
            indices = [i for i in range(len(lmatrices[indiceM]))]
            while not ((indice1 := int(input("Reemplazar matriz - Ingrese índice 1: "))-1) in indices):
                print('Indice Inexistente. Intente nuevamente')
            indice2 = indice1
            if opcion1 != '4':
                while not ((indice2 := int(input("Reemplazar matriz - Ingrese índice 2: "))-1) in indices):
                    print('Indice Inexistente. Intente nuevamente')
            if len(matriz1 := lmatrices[indiceM][indice1]) == len(matriz2 := lmatrices[indiceM][indice2]):
                matriz_res = []
                if opcion1 == '1':
                    matriz_res = [[matriz1[f][c]+matriz2[f][c] for c in range(len(matriz1[indice1]))] for f in range(len(matriz1))]
                elif opcion1 == '2':
                    matriz_res = [[matriz1[f][c]-matriz2[f][c] for c in range(len(matriz1[indice1]))] for f in range(len(matriz1))]
                elif opcion1 == '3':
                    matriz_res = [[matriz1[f][c]*matriz2[f][c] for c in range(len(matriz1[indice1]))] for f in range(len(matriz1))]
                elif opcion1 == '4':
                    matriz_res = [[matriz1[c][f] for c in range(len(matriz1[indice1]))] for f in range(len(matriz1))]
                if matriz_res:
                    print("Las matrices se operaron exitosamente ")
                print('[1]Guardar matriz en una memoria existente\n[2]Guardar matriz a una nueva memoria\n[3]No Guardar')
                while (opcion1 := input('Guardar Matriz - Seleccionar opción: ')) in '12':
                    indice = 0
                    while opcion1 == '1':
                        print('¿Esta segur@ que desea reemplazar una memoria existente?\n[1]Si\n[2]No')
                        if (opcion2 := input("Reemplazar matriz - Seleccionar opción: ")) in '12':
                            if opcion2 == '1':
                                for i, matriz in enumerate(lmatrices[indiceM]):
                                    print(f'Matriz {i + 1}: {len(matriz)}x{len(matriz[0])}')
                                while not ((indice := int(input("Reemplazar matriz - Ingrese índice: "))) in
                                           [i for i in range(1, len(lmatrices[indiceM]) + 1)]):
                                    print('Indice Inexistente. Intente nuevamente')
                                lmatrices[indiceM].remove(lmatrices[indiceM][indice - 1])
                        else:
                            print('Opción Inexistente. Intente nuevamente')
                    lmatrices[indiceM].append(matriz_res) if opcion1 == '2' else lmatrices[indiceM].insert(indice - 1, matriz_res)
                    print("La matriz se guardo exitosamente ")
                    break
                else:
                    if opcion1 != '3':
                        print('Opción Inexistente. Se descartó la última operación')
                print('[1]Sumar\n[2]Restar\n[3]Multiplicar\n[4]Trasponer\n[5]Salir')
            else:
                print("¡Vaya! parece que las dimensiones de ambas matrices no coincide. Seleccione dos matrices válidas")
        else:
            if opcion1 != '5':
                print('Opción Inexistente. Intente nuevamente')
                OperarMatrices(lmatrices,indiceM)
    else:
        print("¡Vaya! parece que aún no hay matrices guardadas. Ingrese 2 o más matrices")
        IngresarMatrices(lmatrices,indiceM)

# Función Mostrar Matrices
def MostrarMatrices(lmatrices,indiceM):
    print('[1]Listar Matrices\n[2]Escoger Matriz\n[3]Finalizar')
    while (opcion := input('Mostrar Matrices - Seleccionar opción: ')) in '12':
        if not(lmatrices[indiceM] == []):
            for i, matriz in enumerate(lmatrices[indiceM]):
                print(f'Matriz {i + 1}: {len(matriz)}x{len(matriz[0])}')
            print('[1]Listar Matrices\n[2]Escoger Matriz\n[3]Finalizar')
        else:
            print("¡Vaya! parece que aún no hay matrices guardadas. Ingrese una matriz")
            IngresarMatrices(lmatrices,indiceM)
        if opcion == '2':
            matriz = int(input('Ingrese numero de Matriz: ')) - 1
            for f, fila in enumerate(lmatrices[indiceM][matriz]):
                for c, columna in enumerate(fila):
                    print(' ', lmatrices[indiceM][matriz][f][c], end='')
                print()
            print('[1]Listar Matrices\n[2]Escoger Matriz\n[3]Finalizar')
    else:
        if opcion != '3':
            print('Opción Inexistente. Intente nuevamente')
            MostrarMatrices(lmatrices,indiceM)

# Función Finalizar
def Finalizar():
    global menu
    menu = '4'
    print('Proceso finalizado')

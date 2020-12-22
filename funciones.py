from menus import *
import json

# Función Ingresar Matrices
def IngresarMatrices(lmatrices, indiceM, guardar=False, new_matriz=0):
    while True:
        confirmacion = 0
        indice = 0
        opcion = MenuIngresarMatrices()
        if opcion == '1':
            while True:
                print('¿Esta segur@ que desea reemplazar una memoria existente?\n[1]Si\n[2]No')
                confirmacion = input("Reemplazar matriz - Seleccionar opción: ")
                if confirmacion == '1':
                    for i, matriz in enumerate(lmatrices[indiceM]):
                        print(f'Matriz {i + 1}: {len(matriz)}x{len(matriz[0])}')
                    while not (indice := int(input("Reemplazar matriz - Ingrese índice: ")) in [i for i in range(1, len(
                            lmatrices[indiceM]) + 1)]):
                        print('Indice Inexistente. Intente nuevamente')
                    lmatrices[indiceM].remove(lmatrices[indiceM][indice - 1])
                    break
                elif confirmacion == '2':
                    break
                print('Opción Inexistente. Intente nuevamente')
        if confirmacion == '2':
            break
        if opcion in '12' and not guardar:
            new_matriz = [[int(j) for j in input(f"Ingresar Matriz - Elementos de fila {i + 1}: ").split(",")]
                          for i in range(int(input("Ingresar Matriz - Número de filas: ")))]
            for f in new_matriz:
                if len(new_matriz[0]) != len(f):
                    print("¡Vaya! parece que el numero de columnas no coincide porfavor inserte una matriz valida")
                    new_matriz = None
            laberinto = False
            for i in range(len(new_matriz)):

                for j in range(len(new_matriz[i])):
                    if not(new_matriz[i][j]  in [0, 1]):
                        laberinto = True
            if new_matriz:
                lmatrices[indiceM].append(new_matriz) if opcion == '2' else lmatrices[indiceM].insert(indice - 1, new_matriz)
                if not laberinto:
                    while True:
                        print("El laberinto se guardó exitosamente. ¿Desea resolver el laberinto?\n[1]Si\n[2]No")
                        confirmacion_lab = input("Resolver laberinto - Seleccionar opción: ")
                        if confirmacion_lab == '1':
                            solve_laberinto(new_matriz)
                            break
                        elif confirmacion_lab == '2':
                            break
                        print('Opción Inexistente. Intente nuevamente')
                else:
                    print("La matriz se guardó exitosamente ")
        else:
            if opcion == '3':
                break
            if guardar:
                lmatrices.append(new_matriz) if opcion == '2' else lmatrices.insert(indice - 1, new_matriz)
                print("salio ")
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
                while not ((indice1 := int(input("Operar matriz - Ingrese índice 1: ")) - 1) in indices):
                    print('Indice Inexistente. Intente nuevamente')
                indice2 = indice1
                if operacion != '4':
                    while not ((indice2 := int(input("Operar matriz - Ingrese índice 2: ")) - 1) in indices):
                        print('Indice Inexistente. Intente nuevamente')
                matriz_res = []
                if len(matriz1 := lmatrices[indiceM][indice1]) == len(matriz2 := lmatrices[indiceM][indice2]):
                    if operacion == '1':
                        matriz_res = [[matriz1[f][c] + matriz2[f][c] for c in range(len(matriz1))] for f in
                                      range(len(matriz1))]
                    elif operacion == '2':
                        matriz_res = [[matriz1[f][c] - matriz2[f][c] for c in range(len(matriz1))] for f in
                                      range(len(matriz1))]
                if operacion == '3' and len(matriz1[0]) == len(matriz2):
                    for i in range(len(matriz1)):
                        matriz_res.append([])
                    for f in range(len(matriz1)):
                        for c in range(len(matriz2[f])):
                            temp = 0
                            for i in range(len(matriz1)):
                                temp += matriz1[f][i] * matriz2[i][c]
                            matriz_res[f].append(temp)
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
                    print(
                        "¡Vaya! parece que las dimensiones de ambas matrices no coincide. Seleccione dos matrices válidas")
                if (operacion := MenuOperarMatrices()) == '5':
                    break

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
def Finalizar(lmatrices,users):
    import sys
    memoria = open('memoria.txt', 'r+')
    memoria_users = open('memoria_users', 'r+')
    json.dump(lmatrices, memoria)
    json.dump(users, memoria_users)
    memoria.close()
    memoria_users.close()
    print('Proceso finalizado! Gracias')
    sys.exit()


# Laberinto
def solve_laberinto(laberinto):
    # Tamaño_del_laberinto
    N = len(laberinto)
    M = len(laberinto[0])
    def is_safe(laberinto, x, y):
        # Funcion utilitaria que verifica si x, y son indices validos
        if 0 <= x < N and 0 <= y < M and laberinto[x][y] == 1 and sol[x][y] != 1:
            return True
        return False
    def print_solution(sol):
        # Funcion utilitaria para imprimir la solución de la matriz
        for i in sol:
            for j in i:
                print(str(j) + " ", end="")
            print("")
    # Función Recursiva utilitaria para resolver el problema del laberinto
    def solve_laberinto_util(laberinto, x, y, sol):
        # if (x, y is goal) return True
        if x == N - 1 and y == M - 1:
            sol[x][y] = 1
            return True
        # verificar si laberinto[x][y] es valido
        if is_safe(laberinto, x, y):
            # marcar x, y como parte de la solución
            sol[x][y] = 1
            # movemos hacia adelante
            if solve_laberinto_util(laberinto, x + 1, y, sol):
                return True
            # si moviendo hacia adelante no nos da la solución
            # #entonces movemos hacia abajo
            if solve_laberinto_util(laberinto, x, y + 1, sol):
                return True
            # hacia atras
            if y >= 1 and solve_laberinto_util(laberinto, x, y - 1, sol):
                return True
            # hacia arriba
            if x >= 1 and solve_laberinto_util(laberinto, x - 1, y, sol):
                return True
            # si ninguno de los movimientos funciona
            # #BACKTRACK: desmarcamos x, y como parte de la solución
            sol[x][y] = 0
            return False
        return False

    sol = [[0 for i in range(M)] for j in range(N)]
    if not solve_laberinto_util(laberinto, 0, 0, sol):
        print("No existe Solución")
        return False
    print_solution(sol)
    return True

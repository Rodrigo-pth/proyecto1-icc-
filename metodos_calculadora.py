# Función Ingresar Matrices
from Menus import *

def creaMatriz():
    # crear matriz
    new_matriz = [[int(j) for j in input(f"Elementos de fila {i + 1}: ").split(",")]
                  for i in range(int(input("Ingrese el número de filas: ")))]
    # comprobar si es una matriz
    for f in new_matriz:
        if len(new_matriz[0]) != len(f):
            print("¡Vaya! parece que el numero de columnas no coincide porfavor inserte una matriz valida")
            new_matriz = None
            break
    return new_matriz

def IngresarMatrices(lmatrices,indiceM,L_operar=True,new_matriz = 0):
    while (opcion1 := MenuIngresarMatrices()) != '3':
        indice = 0
        while opcion1 == '1' :
            print('¿Esta segur@ que desea reemplazar una memoria existente?\n[1]Si\n[2]No')
            if (opcion2 := input("Reemplazar matriz - Seleccionar opción: ")) in '12':
                if opcion2 == '1' and MostrarMatrices(lmatrices,indiceM,2):
                    while not((indice := int(input("Reemplazar matriz - Ingrese índice: "))) in
                              [i for i in range(1, len(lmatrices[indiceM])+1)]):
                        print('Indice Inexistente. Intente nuevamente')
                    lmatrices[indiceM].remove(lmatrices[indiceM][indice-1])

                else:
                    opcion1 = False
                break
            else:
                print('Opción Inexistente. Intente nuevamente')
        if opcion1 and L_operar:
            # crear matriz
            new_matriz = [[int(j) for j in input(f"Elementos de fila {i + 1}: ").split(",")]
                          for  i in range(int(input("Ingrese el número de filas: ")))]
            # comprobar si es una matriz
            for f in new_matriz:
                if len(new_matriz[0]) != len(f):
                    print("¡Vaya! parece que el numero de columnas no coincide porfavor inserte una matriz valida")
                    new_matriz = None
                    break
            if new_matriz:
                lmatrices[indiceM].append(new_matriz) if opcion1 == '2' else lmatrices[indiceM].insert(indice - 1, new_matriz)
                print("La matriz se guardo exitosamente ")
        elif L_operar == False:
            lmatrices[indiceM].append(new_matriz) if opcion1 == '2' else lmatrices[indiceM].insert(indice - 1,new_matriz)
            print("La matriz se guardo exitosamente ")

    else:
        print('Salio de Ingresar Matrices') if L_operar else print("salio de guardar matrices")

# Función Operar Matrices
def OperarMatrices(lmatrices,indiceM):
    if not (lmatrices[indiceM] == []):
        while (opcion1 := MenuOperarMatrices()) != '5':
            MostrarMatrices(lmatrices,indiceM,2)
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
                    for f, fila in enumerate(matriz_res):
                        for c, columna in enumerate(fila):
                            print(' ', matriz_res[f][c], end='')
                        print()
                IngresarMatrices(lmatrices,indiceM,False,matriz_res)
            else:
                print("¡Vaya! parece que las dimensiones de ambas matrices no coincide. Seleccione dos matrices válidas")
        else:
            print('Salio de Operar Matrices')
    else:
        print("¡Vaya! parece que aún no hay matrices guardadas. Ingrese 2 o más matrices")
        IngresarMatrices(lmatrices,indiceM)

# Función Mostrar Matrices
def MostrarMatrices(lmatrices,indiceM,EnFMostrar=1):
    while EnFMostrar == 2 or (opcion := MenumostrarMatrices()) != '3':
        if not(lmatrices[indiceM] == []):
            for i, matriz in enumerate(lmatrices[indiceM]):
                print(f'Matriz {i + 1}: {len(matriz)}x{len(matriz[0])}')
            if EnFMostrar == 2:
                return True
            if opcion == '2':
                matriz = int(input('Ingrese numero de Matriz: ')) - 1
                for f, fila in enumerate(lmatrices[indiceM][matriz]):
                    for c, columna in enumerate(fila):
                        print(' ', lmatrices[indiceM][matriz][f][c], end='')
                    print()
        else:
            print("¡Vaya! parece que aún no hay matrices guardadas. Ingrese una matriz")
            return False
    else:
        print('Salio de Mostrar Matrices')


# Función Finalizar
def Finalizar():
    global menu
    menu = '4'
    print('Proceso finalizado')

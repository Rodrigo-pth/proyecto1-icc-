# Calculadora de Matrices
# Menú:
print('[1]Ingresar Matrices\n[2]Operar Matrices\n[3]Mostrar Matrices\n[4]Finalizar')
lmatrices = [[[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]], 
             [[1, 2, 3], 
              [4, 5, 6], 
              [6, 7, 8]]] #Ejemplo
while (menu := int(input('Menú - Seleccionar opción: '))) != 4:
    if menu in [1, 2]:
        # Función Ingresar Matrices
        def IngresarMatrices():
            print(lmatrices)
        # Función Operar Matrices
        def OperarMatrices():
            matriz_res = []
            print(matriz_res)
        IngresarMatrices() if menu == 1 else OperarMatrices()
        
    elif menu in [3, 4]:
        # Función Mostrar Matrices
        def MostrarMatrices():
            print('[1]Listar Matrices\n[2]Escoger Matriz\n[3]Finalizar')
            opcion = int(input('Mostrar Matriz - Seleccionar opción: '))
            if opcion == 1:
                for i, matriz in enumerate(lmatrices):
                    print(f'Matriz {i+1}: {len(matriz)}x{len(matriz[0])}')
            elif opcion == 2:
                for i, matriz in enumerate(lmatrices):
                    print(f'Matriz {i+1}: {len(matriz)}x{len(matriz[0])}')
                matriz = int(input('Ingrese numero de Matriz: '))-1
                for f, fila in enumerate(lmatrices[matriz]):
                    for c, columna in enumerate(fila):
                        print(' ', lmatrices[matriz][f][c], end='')
                    print()
        # Función Finalizar
        def Finalizar():
            global menu
            menu = 4
            print('Proceso finalizado')
        MostrarMatrices() if menu == 3 else Finalizar()
        
    else:
        print('Opción Incorrecta. Intente nuevamente')

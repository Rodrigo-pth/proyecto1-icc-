# Calculadora de Matrices
from metodos_calculadora import *
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
        MostrarMatrices() if menu == 3 else Finalizar()
    else:
        print('Opción Incorrecta. Intente nuevamente')

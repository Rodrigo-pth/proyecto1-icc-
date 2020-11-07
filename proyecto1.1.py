# Calculadora de Matrices
Users_List = []
Matrix_List = []
print("BIENVENIDO A TU CALCULADORA DE MATRICES FAVORITA ")
name = str(input("Ingrese su nombre de usuario: "))
if name in Users_List:
    indice = Users_List.index(name)
else:
    indice = len(Users_List)
    Users_List.append((name))
    Matrix_List.append(([]))

#aqui el menu
from metodos_calculadora import *
from up_matrix import *
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
        IngresarMatrices(Matrix_List,indice) if menu == 1 else OperarMatrices()
    elif menu in [3, 4]:
        MostrarMatrices(Matrix_List[indice]) if menu == 3 else Finalizar()
    else:
        print('Opción Incorrecta. Intente nuevamente')
    print('[1]Ingresar Matrices\n[2]Operar Matrices\n[3]Mostrar Matrices\n[4]Finalizar')
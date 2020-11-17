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

# Calculadora de Matrices
from metodos_calculadora import *
print("BIENVENIDO A TU CALCULADORA DE MATRICES FAVORITA!")
# Menú:
lmatrices = [[[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]],
             [[1, 2, 3],
              [4, 5, 6],
              [6, 7, 8]]]
print('[1]Ingresar Matrices\n[2]Operar Matrices\n[3]Mostrar Matrices\n[4]Finalizar')
while (menu := input('Menú - Seleccionar opción: ')) != '4':
    if menu in '12':
        IngresarMatrices(lmatrices) if menu == '1' else OperarMatrices(lmatrices)
    elif menu in '34':
        MostrarMatrices(lmatrices) if menu == '3' else Finalizar()
    else:
        print('Opción Inexistente. Intente nuevamente')
    print('[1]Ingresar Matrices\n[2]Operar Matrices\n[3]Mostrar Matrices\n[4]Finalizar')

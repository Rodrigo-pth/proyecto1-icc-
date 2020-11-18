# Calculadora de Matrices
lmatrices = [[[[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]],
             [[1, 2, 3],
              [4, 5, 6],
              [6, 7, 8]]],
             [[[1, 3, 1, 7],
               [2, 2, 6, 3],
               [8, 7, 10, 5]],
              [[1, 1, 3],
               [7, 4, 2]]]]
Users_List = ["Alex", "Samuel"]
print("BIENVENIDO A TU CALCULADORA DE MATRICES FAVORITA ")
name = str(input("Ingrese su nombre de usuario: "))
if name in Users_List:
    indiceM = Users_List.index(name)
else:
    indiceM = len(Users_List)
    Users_List.append((name))
    lmatrices.append(([]))

# Calculadora de Matrices
from metodos_calculadora import *
print("BIENVENIDO A TU CALCULADORA DE MATRICES FAVORITA!")
# Menú:
print('[1]Ingresar Matrices\n[2]Operar Matrices\n[3]Mostrar Matrices\n[4]Finalizar')
while (menu := input('Menú - Seleccionar opción: ')) != '4':
    if menu in '12':
        IngresarMatrices(lmatrices,indiceM) if menu == '1' else OperarMatrices(lmatrices,indiceM)
    elif menu in '34':
        MostrarMatrices(lmatrices,indiceM) if menu == '3' else Finalizar()
    else:
        print('Opción Inexistente. Intente nuevamente')
    print('[1]Ingresar Matrices\n[2]Operar Matrices\n[3]Mostrar Matrices\n[4]Finalizar')

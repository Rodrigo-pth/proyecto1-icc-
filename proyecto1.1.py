# Calculadora de Matrices
from Menus import *
from metodos_calculadora import *
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
# Identificacion de usuario
name = str(input("Ingrese su nombre de usuario: "))
if name in Users_List:
    indiceM = Users_List.index(name)
else:
    indiceM = len(Users_List)
    Users_List.append((name))
    lmatrices.append(([]))
# Menú:

while (menu := MenuPrincipal()) != '4':
    if menu in '12':
        IngresarMatrices(lmatrices,indiceM) if menu == '1' else OperarMatrices(lmatrices,indiceM)
    else:
        MostrarMatrices(lmatrices,indiceM) if menu == '3' else Finalizar()

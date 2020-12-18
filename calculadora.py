# Calculadora de Matrices
from funciones import *
import json
# Ingreso:
print("BIENVENIDO A TU CALCULADORA DE MATRICES FAVORITA!")
memoria = open('memoria.txt', 'r')
lmatrices = json.loads(memoria.read())
memoria.close()
users = ["Administrador", "Invitado"]
if (user := input("Ingrese su usuario: ")) in users:
    indiceM = users.index(user)
else:
    indiceM = len(users)
    users.append(user)
    lmatrices.append([])
# Menú
while True:
    print('[1]Ingresar Matrices\n'
          '[2]Operar Matrices\n'
          '[3]Mostrar Matrices\n'
          '[4]Finalizar')
    menu = input('Menú - Seleccionar opción: ')
    if menu in '12':
        IngresarMatrices(lmatrices, indiceM) if menu == '1' else OperarMatrices(lmatrices, indiceM)
        memoria.close()
    elif menu in '34':
        MostrarMatrices(lmatrices, indiceM) if menu == '3' else Finalizar()
    else:
        print('Opción Inexistente. Intente nuevamente')

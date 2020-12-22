# Calculadora de Matrices
from funciones import *
import json

# Iniciar Sesión
print("BIENVENIDO A TU CALCULADORA DE MATRICES FAVORITA!")
memoria = open('memoria.txt', 'r+')
memoria_users = open('memoria_users', 'r+')
lmatrices = json.loads(memoria.read())
users = json.loads(memoria_users.read())
memoria.close()
memoria_users.close()
if (user := input("Ingrese su usuario: ")) in users:
    indiceM = users.index(user)
else:
    indiceM = len(users)
    users.append(user)
    lmatrices.append([])
# Menú Principal

while True:
    memoria = open('memoria.txt', 'r+')
    memoria_users = open('memoria_users', 'r+')
    print('[1]Ingresar Matrices\n'
          '[2]Operar Matrices\n'
          '[3]Mostrar Matrices\n'
          '[4]Finalizar')
    menu = input('Menú - Seleccionar opción: ')
    if menu in '12':
        IngresarMatrices(lmatrices, indiceM) if menu == '1' else OperarMatrices(lmatrices, indiceM)

    elif menu in '34':
        MostrarMatrices(lmatrices, indiceM) if menu == '3' else Finalizar(lmatrices,users)
    else:
        print('Opción Inexistente. Intente nuevamente')
    json.dump(lmatrices,memoria)
    json.dump(users,memoria_users)
    memoria.close()
    memoria_users.close()
# Función Ingresar Matrices
def IngresarMatrices():
  print(lmatrices)
  
# Función Operar Matrices
def OperarMatrices():
  matriz_res = []
  print(matriz_res)

# Función Mostrar Matrices
def MostrarMatrices(lmatrices):
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

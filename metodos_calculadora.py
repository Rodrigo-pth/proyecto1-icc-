# Función Ingresar Matrices
def IngresarMatrices(lmatrices):
  print('[1]Ingresar Matriz en una menoria existente\n[2]Ingresar Matriz a una memoria\n[3]Salir')
  indice = 0
  if (opcion := int(input('Ingresar Matrices - Seleccionar opción: '))) != 3:
    if opcion == 1:
      print('¿Esta segur@ que desea reemplazar una memoria existente?\n[1]Si\n[2]No')
      if (int(input("Ingrese la opcion a seguir: "))) == 1:
        for i, matriz in enumerate(lmatrices):
         print(f'Matriz {i + 1}: {len(matriz)}x{len(matriz[0])}')
        indice = int(input("Matriz a sobreescribir: "))
    new_matriz = [[int(j) for j in input(f"Ingrese los elementos de la fila {i + 1}: ").split(",")] 
                  for i in range(int(input("ingrese el numero de filas: ")))]
    for f in new_matriz:
      if len(new_matriz[0]) != len(f):
        print("¡Vaya! parece que el numero de columnas no coincide porfavor inserte una matriz valida")
        new_matriz = None
        break
      if new_matriz:
          lmatrices.append(new_matriz) if opcion == 2 else lmatrices.insert(indice - 1, new_matriz)
          print("La matriz se guardo exitosamente ")
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
    if lmatrices != []:
      for i, matriz in enumerate(lmatrices):
        print(f'Matriz {i+1}: {len(matriz)}x{len(matriz[0])}')
      MostrarMatrices(lmatrices)
    else:
      print("¡Vaya! parece que aún no hay matrices guardadas")
  elif opcion == 2:
    if lmatrices != []:
      for i, matriz in enumerate(lmatrices):
        print(f'Matriz {i+1}: {len(matriz)}x{len(matriz[0])}')
      matriz = int(input('Ingrese numero de Matriz: '))-1
      for f, fila in enumerate(lmatrices[matriz]):
        for c, columna in enumerate(fila):
          print(' ', lmatrices[matriz][f][c], end='')
        print()
      MostrarMatrices(lmatrices)
    else:
      print("¡Vaya! parece que aún no hay matrices guardadas")
      MostrarMatrices(lmatrices)
      
# Función Finalizar
def Finalizar():
  global menu
  menu = 4
  print('Proceso finalizado')

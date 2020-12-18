def MenuIngresarMatrices():
    while True:
        print('[1]Ingresar Matriz en una memoria existente\n'
              '[2]Ingresar Matriz en una nueva memoria\n'
              '[3]Salir')
        if (opcion := input('Ingresar Matrices - Seleccionar opción: ')) in '123':
            return opcion
        print("La opcion que ingreso no se encuentra disponible,  vuelva a intentarlo")

def MenuOperarMatrices():
    while True:
        print('[1]Sumar\n'
              '[2]Restar\n'
              '[3]Multiplicar\n'
              '[4]Trasponer\n'
              '[5]Salir')
        if (opcion := input('Operar Matrices - Seleccionar opción: ')) in '12345':
            return opcion
        print("La opcion que ingreso no se encuentra disponible,  vuelva a intentarlo")

def MenuMostrarMatrices():
    while True:
        print('[1]Listar Matrices\n'
              '[2]Escoger Matriz\n'
              '[3]Finalizar')
        if (opcion := input('Mostrar Matrices - Seleccionar opción: ')) in '123':
            return opcion
        print("La opcion que ingreso no se encuentra disponible,  vuelva a intentarlo")

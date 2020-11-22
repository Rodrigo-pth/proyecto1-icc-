def MenuPrincipal():
    while True:
        print('[1]Ingresar Matrices\n[2]Operar Matrices\n[3]Mostrar Matrices\n[4]Finalizar')
        selec = input("Seleccione opción: ")
        if selec in ["1", "2","3", "4"]:
            return selec
        else:
            print("La opcion que ingreso no se encuentra disponible,  vuelva a intentarlo")



def MenuIngresarMatrices():
    while True:
        print('[1]Ingresar Matriz en una menoria existente\n[2]Ingresar Matriz a una memoria libre\n[3]Salir')
        selec = input("Seleccione opción: ")
        if selec in ["1", "2", "3"]:
            return selec
        else:
            print("La opcion que ingreso no se encuentra disponible,  vuelva a intentarlo")

def MenuOperarMatrices():
    while True:
        print('[1]Sumar\n[2]Restar\n[3]Multiplicar\n[4]Trasponer\n[5]Salir')
        selec = input("Seleccione opción: ")
        if selec in ["1", "2", "3","4", "5"]:
            return selec
        else:
            print("La opcion que ingreso no se encuentra disponible,  vuelva a intentarlo")
def MenumostrarMatrices():
    while True:
        print('[1]Listar Matrices\n[2]Escoger Matriz\n[3]Finalizar')
        selec = input("Seleccione opción: ")
        if selec in ["1", "2", "3"]:
            return selec
        else:
            print("La opcion que ingreso no se encuentra disponible,  vuelva a intentarlo")
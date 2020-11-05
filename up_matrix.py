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

def PedirMatriz():
    filas = int(input("ingrese el numero de filas: "))
    Matriz = [[int(j) for j in input(f"ingrese los elementos de la fila {i+1}: ").split(",")] for i in range(filas)]
    for i in Matriz:
        if len(Matriz[0]) != len(i):
            Matriz = None
            break
    return Matriz



def IngresarMatrices ():
    while True:
        print('[1]Ingresar Matriz en una menoria existente\n[2]Ingresar Matriz a una memoria\n[3]Salir')
        n = int(input("Ingrese la opcion a seguir: "))
        if n == 3:
            print("salio")
            break
        while True:
            if n == 1:
                print("¿Esta segur@ que desea reemplazar una memoria existente?\n Se borrara la informacion  existente\n[1] Yes\n[2] No")
                e = int(input("Ingrese la opcion a seguir: "))
                if e == 2:
                    break
                else:
                    #ListaMatrices()
                    indiceV = int(input("¿Que ma triz desea sobreescribir?"))
            MP = PedirMatriz()
            if MP != None:
                Matrix_List[indice].append(MP) if n == 2 else Matrix_List[indice].insert(indiceV-1,MP )
                print("La matriz se guardo exitozamente ")
            else:
                print("¡Vaya! parece que el numero de columnas no coincide porfavor inserte una matriz valida")
            break

IngresarMatrices()





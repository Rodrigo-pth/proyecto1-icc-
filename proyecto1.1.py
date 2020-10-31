# Calculadora de Matrices
from Metodos_Calculadora import *
# Menú:
menu = int(input('Seleccionar opción: '))
if menu in [1, 2]:
    lmatrices = []
    lmatrices.IngresarMatrices() if menu == 1 else lmatrices.OperarMatrices()

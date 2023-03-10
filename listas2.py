"""
Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100
"""
listaEnteros = [23, 48, 65, 7, 1, 16, 77, 198]
acumulador = 0
for x in range(len(listaEnteros)):
    if listaEnteros[x]>100:
        acumulador = acumulador + 1
print("Lista de 8 enteros por asignación: ")
print(listaEnteros)
print("La cantidad de valores de la lista q almacenan un valor mayor a 100 son: ")
print(acumulador)


"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
"""

alturas = []
suma = 0
altas = 0
bajas = 0

for x in range(5):
    valor = float(input("Digita la altura de la persona: "))
    alturas.append(valor)
    suma = suma + valor

print("lista de alturas: ")
print(alturas)
promedio = suma/5
print("Promedio de alturas es igual a: ", promedio)

for x in range(len(alturas)):
    if alturas[x] > promedio:
        altas = altas + 1
    else:
        bajas = bajas + 1

print("Personas mas altas que el promedio son: ")
print(altas)
print("Personas mas bajas que el promedio: ")
print(bajas)

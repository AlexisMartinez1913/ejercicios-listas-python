"""
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)
"""
nombres = []
sueldos = []

cantidad = int(input("Ingrese la cantidad de empleados que tiene la empresa: "))
for x in range(cantidad):
    nom=input("Ingrese el nombre del empleado: ")
    nombres.append(nom)
    salario = float(input("Ingrese su respectivo sueldo: "))
    sueldos.append(salario)
print()
print("Nombres y su salario: ")
for x in range(cantidad):
    print(nombres[x], sueldos[x])
print()
pos = 0
while pos<(len(nombres)):
    if sueldos[pos]>10000:
        nombres.pop(pos)
        sueldos.pop(pos)
    else:
        pos+=1
print()
print("Nueva lista eliminando nombres de empleados con un sueldo mayor a 10.000: ")
for x in range(len(nombres)):
    print(nombres[x], sueldos[x])
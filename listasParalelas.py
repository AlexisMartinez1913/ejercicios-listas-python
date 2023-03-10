"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. 
Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.
"""
productos = []
precios = []
for x in range(5):
    nombre = input("Ingrese el nombre del producto: ")
    productos.append(nombre)
    valor = int(input("Ingrese el precio del mismo: "))
    precios.append(valor)
cantidad = 0

for x in range(1,5):
    if precios[x]>precios[0]:
        cantidad = cantidad+1

print("Lista de productos")
print(productos)
print("Precios: ")
print(precios)
print("La cantidad de productos que tienen un precio mayor al primero son: ", cantidad)

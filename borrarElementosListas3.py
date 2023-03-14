#Crear una lista de 5 enteros y cargarlos por teclado. 
# Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores

enteros = []
for x in range(5):
    num=int(input("Ingrese un numero entero: "))
    enteros.append(num)
lista = []
print("Lista de enteros: ")
print(enteros)
print()

pos = 0
while pos<(len(enteros)):

    if enteros[pos]>= 10:
        lista.append(enteros.pop(pos))
    else:
        pos+=1

print("Lista borrando los elementos mayores o iguales de 10 ")  
print(enteros) 

print("Lista de elementos mayores o iguales a 10: ")
print(lista)

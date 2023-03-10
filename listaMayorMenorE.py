"""
Cargar una lista con 5 elementos enteros. Imprimir el mayor y
 un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
"""
lista=[]
for x in range(5):
    num = int(input("Ingrese un valor entero: "))
    lista.append(num)

mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor = lista[x]

print("Lista de elementos: ")
print(lista)
print("Mayor elemento de la lista es: ", mayor)
acumulador = 0
for x in range(5):
    if lista[x] == mayor:
        acumulador = acumulador+1

if acumulador>1:
    print("el mayor se repite:  ", acumulador , "veces")

"""
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de persona menor en orden alfabético.
"""
nombres=[]
for x in range(5):
    nom=input("Ingrese el nombre de la persona: ")
    nombres.append(nom)
menor = nombres[0]
for x in range(1,5):
    if nombres[x]<menor:
        menor = nombres[x]
print("Lista de nombres: ")
print(nombres)
print("La persona menor en orden alfabetico es: ", menor)

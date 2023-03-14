lista=[10, 20, 30]
print(len(lista))    # imprime un 3
lista.append(100)
print(len(lista))    # imprime un 4
print(lista[0])      # imprime un 10
print(lista[3])      # imprime un 100

#definimos una lista vacia
lista=[]
#disponemos un ciclo de 5 vueltas
for x in range(5):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

#imprimimos la lista    
print(lista)

lista2=[]
valor1=int(input("Ingresar valor (0 para finalizar):"))
while valor1!=0:
    lista2.append(valor1)
    valor1=int(input("Ingresar valor (0 para finalizar):"))

print("Tamano de la lista:")
print(len(lista2))
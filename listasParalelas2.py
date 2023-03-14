"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. 
En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
"""
nombres = []
notas= []
for x in range(4):
    nom=input("Ingrese el nombre del estudiante: ")
    nombres.append(nom)
    calificacion = float(input("Ingrese su nota del examen: "))
    notas.append(calificacion)

leyenda = 0
for i in range(4):
    print(nombres[i])
    print(notas[i])
    if notas[i]>=8:
        print("Muy bueno")
        leyenda +=1
    elif notas[i]>=4:
        print("Bueno")
    else:
        print("Insuficiente")

print("La cantidad de alumnos que tienen la leyenda 'Muy bueno' son: "  ,leyenda )
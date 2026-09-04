# creando una lista que se puede modificar y que puede contener diferentes tipos de datos
lista = ["carlos", "estudiante", True, 1, 1.60]


# creando una tupla que no se puede modificar y que puede contener diferentes tipos de datos
tupla = ("carlos", "estudiante", True, 1, 1.60)  

 # esto es valido porque las listas son mutables, es decir, se pueden modificar
lista[0] = "juan" 

# es no es valido porque las tuplas son inmutables, es decir, no se pueden modificar
#tupla [0] = "juan"


# creando un conjunto set mo se puede acceder a elementos por su indice, pero si se puede modificar y no permite elementos duplicados
conjunto = {"carlos", "estudiante", True, 1, 1.60}

#print(conjunto[2]) # esto no es valido porque los conjuntos no tienen indice

# creando un diccionario que se puede modificar y que contiene pares de clave-valor

diccionario = {
    "nombre": "carlos",
    "profesion": "estudiante",
    "altura": 1.60
}

print(diccionario["nombre"]) # esto es valido porque los diccionarios tienen clave-valor





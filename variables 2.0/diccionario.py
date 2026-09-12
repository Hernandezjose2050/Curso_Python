#Creando un diccionario con dict()
diccionario  = dict(nombre = "carlos", apellidos="Hernandez")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario1 = {frozenset(["carlos", "hernandez"]):"jajajajjaj"}

#creando diccionarios con fromkeys con dos parametros
diccionario2 = dict.fromkeys(["nombre", "apellidos"])

#creando diccionarios con fromkey() cambiando el valor por defecto "no se"
diccionario2 = dict.fromkeys(["nombre", "apellidos"], "no se")

print(diccionario2)
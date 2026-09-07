
cadena1 = "Hola, ¿cómo estás?"

cadena2 = "Estoy bien, gracias."

# convierte la cadena a mayúsculas
mayuscula = cadena1.upper()

# convierte la cadena a minúsculas
minúsculas = cadena2.lower()

#converte la primera letra de la cadena a mayúscula
primer_letra_a_mayuscula = cadena1.capitalize()

#busqueda de una subcadena dentro de la cadena
busqueda_find = cadena1.find("t")

# busqueda de la posición de una subcadena dentro de la cadena si no se encuentra lanza un error
busqueda_index = cadena1.index("t")

#verifica si la cadena es un número
es_numero = cadena1.isnumeric()

# verifica si la cadena es alfanumérica
es_alfa_numerico = cadena1.isalpha()

# buscamos la cantidad de veces que se repite una subcadena dentro de la cadena
contar_coincedencias = cadena1.count("o")

#contamos cuantos caracteres tiene la cadena
contar_caracteres = len(cadena1)

#verificamos si la cadena empieza con una subcadena específica
empieza_con = cadena1.startswith("Hola")

# la cadena termina con otra cadena con otra cadena dada, si es asi devuelve True, de lo contrario devuelve False
termina_con = cadena1.endswith("estás?")

#remplazamos una subcadena por otra dentro de la cadena
cadena_nueva = cadena1.replace("Hola", "Adiós")


cadena_separada = cadena1.split(",")  #separa la cadena en una lista de subcadenas usando la coma como delimitador

print(cadena_separada)
#creando una funcion de 3 argumentos
#def frases(nombre,apellidos,edad):
 #   return f"hola soy {nombre} {apellidos}, mi edad es {edad}"
#utilizando keyword argumentos
#frase_datos = frases("carlos","hernandez", 31)
#print(frase_datos)
    
#creando la misma funcion son un parametro ya definido pero se puede cambiar al momento de pasarle los datos
def frases(nombre,apellido,adjetivo="rico"):
    return f"hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultado = frases("carlos", "hernandez", adjetivo= "pobre")
print(frase_resultado)

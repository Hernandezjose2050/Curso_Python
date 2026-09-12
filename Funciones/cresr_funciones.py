
#creando una funcion simple
#def saludar():
#    print("hola carlos, como estas")
 
 #ejecutando la funcion simple   
#saludar()


#crear una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        abjetivo = "mujer"
    elif (sexo == "hombre"):
        abjetivo = "titan"
    else:
        abjetivo = "amor"
        
    print(f"hola {nombre}, mi {abjetivo} ¿como estas?")

saludar("Camila", "mujer")
saludar("carlos", "hombre")
saludar("shelo", "no binario")


#crear una funcion que nos retorne valores

def crear_contraseña_random(num):
    chars = "abcdefghij"
    numero_entero = str(num)
    num = int(numero_entero[0])
    cr1 = num - 2
    cr2 = num
    cr3 = num - 5
    contraseña = f"{chars[cr1]}{chars[cr2]}{chars[cr3]}{num * 2}"
    return contraseña, num
    
#desempaquetando la funcion
password, primer_numero = crear_contraseña_random(99)
#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"tu contraseña generada automaticmanete es: {password}")
print(f"el numero utilizado para crear la contrasela fue: {primer_numero}")
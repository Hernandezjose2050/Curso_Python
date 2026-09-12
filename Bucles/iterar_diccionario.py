
diccionario = {
    "nombre": "carlos",
    "apellido": "hernande",
    "edad": 34
}
# recorriendo un diccionario para obtner las claves
for key in diccionario:
    print(f"la claves es: {key}")
    
# recorriendo un diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"las claeve es: {key} y el valor es: {value}")
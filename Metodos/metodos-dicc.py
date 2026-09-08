

# devuelve las claves del diccionario
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

#nos devuelve un objeto dict_keys con las claves del diccionario
claves = diccionario.keys()


#obtiene un elemento del diccionario get(), si no encuenta la clave devuelve None
claves1 = diccionario.get("nombre")


# elimina todos los elementos del diccionario clear()
clavee2 = diccionario.clear

# elimina un elemento del diccionario pop(), si no encuentra la clave devuelve un error
diccionario.pop("edad") 

diccionario_iterable =diccionario.items()

print(diccionario_iterable) 
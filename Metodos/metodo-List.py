#creamos una lista de frutas
lista =list(["manzana", "banana", "cereza", "durazno"])

#devuelve la cantidad de elementos en la lista
cantidad_elementos = len(lista)

#agregamos un elemento al final de la lista
lista.append("naranja") 

#agregamos un elemento en la posición 3 de la lista
lista.insert(3, "kiwi") 

#agregamos varios elementos al final de la lista
lista.extend(["pera", "uva"])

#eliminamos el último elemento de la lista
lista.pop(0)

#eliminamos un elemento de la lista por su valor
lista.remove("cereza")

#eliminamos todos los elementos de la lista
#lista.clear()

#ordenamos la lista de forma ascendente ojo solo funciona con elementos del mismo tipo numero
lista.sort()

#invertimos el orden de la lista ojo solo numeros y strings
lista.reverse()


print(lista)
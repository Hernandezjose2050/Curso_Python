
#recorriendo una lista de frutas 
frutas = ["pera","manzana","kiwi","lulo"]



numeros = [10,2,3,5]


for fruta in frutas:
    print(f"ahora la fruta que tenemos son {fruta} ")

#recorriendo una lista de numeros y multiplicarlos por 2
for numero in numeros:
    resultado = numero *2
    print(resultado)
    
    #recorriendo dos lista desde mismo tamaño al mismo tiempo  
for fruta,numero in zip(frutas,numeros):
    print(fruta)
    print(numero)
 
#forma ni optima de recorrer una lista   
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el valor del indice {indice} es: {valor}") 
    
#usando en else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
    
else:
    print("el bucle termino")


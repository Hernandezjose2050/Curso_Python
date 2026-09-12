#forma no optima para sumar valores en funcion
#def suma(lista):
 #   numero_sumado =0 
  #  for numero in lista:
   #     numero_sumado = numero_sumado + numero
    #return numero_sumado
#resultado = suma([8,5,6])
#print(resultado)

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado1 = suma_total([4,5,6])
print(resultado1)

#lo mismo que la funcion anterior pero utilizando el parametro correcto args
def suma(*numeros):
    return sum(numeros) 
resultado = suma(4,5,6)
print(resultado)


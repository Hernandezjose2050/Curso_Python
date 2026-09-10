
numeros = [1,2,3,4,5,6]

#creando una funcion lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x*2

#creando funcion comun que diga su es par o no
#def es_par(num):
 #   if (num%2==0):
  #      return True
       
#usando filtrar con una funcion comun
#numero_pares = filter(es_par,numeros)

#creando lo mismos pero con la funcion lambda
numeros_pares = filter(lambda numero:numero %2 == 0, numeros)  

print(list(numeros_pares))
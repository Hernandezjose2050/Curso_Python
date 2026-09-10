#creando un conjunto con set
conjunto = set(["dato1", "dato2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato3","datos4"])
conjunto2 = {conjunto1, "datos5"}


#print(conjunto2)

#teoria de conjuntos

conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto4.issubset(conjunto3)
resultado = conjunto4 <= conjunto3

#verificando si es un siperconjunto
resultado1 = conjunto4.issuperset(conjunto3)
resultado1 = conjunto4 >= conjunto3

#verificar si hay algun numero en comun
resultado2 = conjunto3.isdisjoint(conjunto4)


print(resultado2)
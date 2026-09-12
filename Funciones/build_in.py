
numero = {5,3,7,8,9}

#encontrando el numero mas alto de una lista
numero_mas_alto = max(numero)
print(numero_mas_alto)


#encontrando el numero mas bajo de una lista
numero_mas_bajo = min(numero)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero_redondeado = round(13.345678,3)
print(numero_redondeado)

#retorna false ->0, vacio, false, none \ distinti a 0 , true, cadena de texto o datos no vacio
resultado_bool = bool("carlos")
print(resultado_bool)

#retorna true, si todos los valores son verdaderos
resultado_all = all([234,"true", [344,23]])
print(resultado_all)

#suma todos los valores en un iterable
suma_total = sum(numero)
print(suma_total)
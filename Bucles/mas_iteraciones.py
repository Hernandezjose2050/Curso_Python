
frutas = ["banana", "pera", "naranja", "manzana"]
candena = "carlos jose"
numeros = [1,2,3,4,5,6,7,8,9]

# se limita que se coma una fruta con la sentencia continue
for fruta in frutas:
    if fruta == "pera":
        continue
    print(f"la fruta que no me voy a comer es: {fruta}")
 
print("--------------------------------------------")    

# evitar que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == "banana":
        break
    print(f"la fruta que no me voy a comer es: {fruta}")
    

#rocorrer una cadena de texto

for letra in candena:
    print(letra)

# for en una sola linea de codigo
numero_duplicados = [x*2 for x in numeros ]
print(numero_duplicados)

#Crear una lista del 1 al 10 y luego crear una lista de números pares del 1 al 10. 
#Creo colección.
numeros=[numeros for numeros in range(1,11)]
print(numeros)

#Ahora es imprimir la colección creada pero con el condicional de solamente los pares. 
numeros=[numeros for numeros in range(1,11) if numeros%2==0]
print(numeros)
#Escribir un programa en python que permita imprimir solo los numeros impares entre 10 y 20. Deben hacerse una versión con for y otra con el bucle while.
for i in range(10,20):
    if i%2==1:
        print(i)

numeros=10 
while numeros<20:
    numeros+=1 
    if numeros%2==0:
        continue #Esta palabra hace que al verificar que es par salta el código y pasa a la iteración siguiente.
    print(numeros)
        
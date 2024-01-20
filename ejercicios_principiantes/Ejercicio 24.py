#Escribir un programa que muestre la tabla de multipliacacion del numero 8. 

a=8 #Numero para el que queremos la tabla de multiplicacion.
i=0 #Numero por el que empieza la tabla. 

for i in range(11):
    print(f"{a} X {i} = {a*i}")

#Bucle externo (aunque no seria necesario porque solo tiene una iteracion)    
for i in [a]: #Aqui colocamos el numero sobre lo que queremos iterar.
    #Bucle interno para la multiplicacion.
    for a in range (11):
        print(f"{i} X {a} = {i*a}")
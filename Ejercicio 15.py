#Escribir un programa que cree la lista L asignándole el valor [1,2,3,4,5,6,7,8,9,10]. Luego crear una nueva lista L1 que recupera un elemento cada tres en la lista L. En este caso debemos obtener como resultado final la siguiente lista [1,4,7,10]. 
L=[]

L2=[]

caracteres=[1,2,3,4,5,6,7,8,9,10]

for caracter in caracteres: 
    L.append(caracter)

print('Lista L:',L)

for caracter in range(1,11,3):
    L2.append(caracter)

print('Lista L2:',L2) 

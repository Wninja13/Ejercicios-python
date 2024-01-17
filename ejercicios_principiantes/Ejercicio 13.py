#Escribir unn programa que permita crear la lista L asignádole los valores[3,2,2,1,9,1,2,3,7] para calcular la cantidad e apiriciones del numero 1 en la lista L. 
L=[3,2,2,1,9,1,2,3,7]
contador=0
for i in L: 
    if i ==1: 
        contador+=1
print(contador)

#Tambien puede usarse un método .count().
L=[3,2,2,1,9,1,2,3,7]
print(L.count(1))

#Hacer un programa que permita creas una lista vacía L y que se agreguen los caracteres 10,25,30,45,90 y las cadenas 'ab','cd','ef'.
L=[]
caracteres=[10,25,30,45,90,'ab','cd','ef']
for caracteres in caracteres: 
    L.append(caracteres)
print("Lista L contiene los siguientes caracteres:",L)

#Tambien puede hacerse de otro modo. Puede usarse operadores para concatenar.
L+=[10,25,30,45,90,'ab','cd','ef']
print(L)
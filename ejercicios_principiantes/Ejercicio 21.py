#Debe escribirse un programa que permita sumar cada uno de los valores del siguiente diccionario:
#La primer solucion es un tanto deficiente dado 
frutas={
    'Manzana':15,
    'Banana':8,
    'Frutilla':12,
    'Kiwi':9, 
    'Durazno':2
}

a=frutas['Manzana']
b=frutas['Banana']
c=frutas['Frutilla']
d=frutas['Kiwi']
e=frutas['Durazno']

print(a+b+c+d+e)

#Metodo alternativo. 

total_frutas=sum(frutas.values())

print(total_frutas)
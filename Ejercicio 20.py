#Debe escribirse un programa que muestre en la consola el valor de las claves 'Manzana' y 'Banana'. 

frutas={'Manzana':3,
        'Banana':7,
        'Kiwi':1
        }
f=frutas.get('Manzana') #Se utiliza metodo get para conseguir el valor de cada objeto.
g=frutas.get ('Banana')
print(f,g)

#Otra forma de resolverlo seria.
frutas={'Manzana':3,
        'Banana':7,
        'Kiwi':1
        }
print(frutas['Manzana'])
print(frutas['Banana'])
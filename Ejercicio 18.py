#Escribir un programa que permita ordenar las tuplas L en orden ascendente desde el segundo elemento. El resultado debe ser L=[("Melocotón",2),("Banana",8), ("Kiwi",9),("fresa",12),("Manzana",15)]
def ordenar_tupla(L):
    lista=list(L)
    longitud=len(L)
    
    for i in range(longitud): 
        for j in range(0,longitud-1): 
             if lista[j][1] > lista[j+1][1]: 
                lista[j],lista[j+1]=lista[j+1],lista[j]
     
    tupla_ordenada=tuple(lista)
    return tupla_ordenada

L=[("Manzana",15),("Banana",8), ("Fresa",12),("Kiwi",9),("Melocotón",2)]
inicio=1

tupla_ordenada=ordenar_tupla(L)
print(tupla_ordenada)

    
         
#Debe escribirse un programa que elimine el elemento de la siguiente lista (el elemento a eliminar es el numero 1):
L=[1,2,3,4,5]
L.pop(0) #Al utilizar pop se quita el elemento en funcon de su numero de indice.
print(L)

#Otro metodo puede ser con remove. La diferencia es que se elimina el valor especifico de una lista, no por su indice, sino por su elemento especifico. 
L2=[1,2,3,4,5]
L2.remove(1)
print(L2)
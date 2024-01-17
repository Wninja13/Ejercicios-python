#Escriba un programa que dadas dos listas L1 y L2, devuelva la lista L3 y que contenga los elementos comunes de la lista L1 y L2. 
L1=[9,8,7,14,3,2,"a","p","hola","b"]

L2=["b",1,9.2,6,3,9,"p"]

#Necesito para poder hacer este ejercicio en primer lugar iterar cada una de estas listas que tengo para poder comprarlas. Para eso #debería crear un for que itere en cada una de ellas e inestar un condicional que permita comprobar la condición que pretendo #aplicar. En este caso la condición debería ser "si el contendio de la lista L1 es igual al de la L2 debe dar verdadero." Tambien #lo que puede hacerse es una lista de comprensión.  Una lista de comprensión en Python es una forma concisa de crear una nueva #lista aplicando una expresión a cada elemento de otra lista (o cualquier iterable) y, opcionalmente, filtrando los elementos que #cumplen ciertas condiciones.

L3=[str(a) for a in L1 if str(a) in map(str, L2)] 
print(L3)
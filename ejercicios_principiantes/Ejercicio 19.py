#Debo escribir un programa que permita invertir una cadena de caracteres. La variable "ch" debe contener la siguiente frase a invertir: "Hola a todos."

ch="Hola a todos."[::-1]
print(ch)

#Otro camino posible podria ser con una funcion. El string seria el argumento y devuelve el string al reves. Al llamar la funcion con el string como parametro y luego se imprime. 
def ch1(x):
    return x[::-1]

respuesta=ch1("Hola a todos.")

print(respuesta)
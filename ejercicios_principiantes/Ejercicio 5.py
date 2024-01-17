#Crear una variable "var" y asignarle un valor "Hola". Luego el programa debe verificar si la variable var es un entero o una cadena de texto. Si es un entero, el programa debe imprimir en la consola "entero" y si es una cadena de caracteres debe imprimir "Cadena de caracteres". 
var='5'

if type(var)==str:
    print('Cadena de caracteres.')
else:
    print('Entero')
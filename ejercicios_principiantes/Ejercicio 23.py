# Escribir un programa que permita formatear la cadena de caracteres: "Me llamo miNombre y tengo edad años. Estoy aprendiendo el Lenguaje"
#El programa debe permitir formatear la cadena asignadole el contenido de las variables miNombre, edad y lenguaje. 

miNombre='German'
edad=33
lenguaje='Python'

print(f"Me llamo {miNombre} y tengo {edad} años. Estoy aprendiendo {lenguaje}.")

# Como resolucion alternativa podria usarse un diccionario con los atributos de cada uno de los elementos. 

datos_persona={
    'miNombre': 'Alex',
    'edad': 22,
    'lenguaje': 'JavaScript'
}

mensaje="Me llamo {miNombre} y tengo {edad} años. Estoy aprendiendo {lenguaje}.".format(**datos_persona)

print(mensaje)

# Una manera alternativa seria crear distintas personas con diferentes atributos dentro de un diccionario. 

datos2={
    'persona_1':{'miNombre': 'German', 'edad': 33, 'lenguaje': 'Python'},
    'persona_2':{'miNombre': 'Julian', 'edad': 55, 'lenguaje': 'C++' },
    'persona_3':{'miNombre': 'Alvaro', 'edad': 24, 'lenguaje': 'C*' },
    'persona_4':{'miNombre': 'Roberto', 'edad': 45, 'lenguaje': 'Ruby' },
}

persona_1_nombre = datos2['persona_1']['miNombre']
persona_2_edad = datos2['persona_2']['edad']

mensaje_persona_1 = "Me llamo {miNombre} y tengo {edad} años. Estoy aprendiendo {lenguaje}.".format(**datos2['persona_1'])
mensaje_persona_2 = "Me llamo {miNombre} y tengo {edad} años. Estoy aprendiendo {lenguaje}.".format(**datos2['persona_2'])
mensaje_persona_3 = "Me llamo {miNombre} y tengo {edad} años. Estoy aprendiendo {lenguaje}.".format(**datos2['persona_3'])

mensaje_persona_4 = "Me llamo {miNombre} y tengo {edad} años. Estoy aprendiendo {lenguaje}.".format(**datos2['persona_4'])

print(mensaje_persona_1)
print(mensaje_persona_2)
print(mensaje_persona_3)
print(mensaje_persona_4)
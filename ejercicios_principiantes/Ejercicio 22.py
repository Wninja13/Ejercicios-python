#Escribir un programa que permita truncar un numero decimal a dos cifras despues de la coma. Por ejemplo si se toma el numero 187,632587 en la consolase debe imprimir 187,63.
print("{:.2f}".format(187.632587))

#Solucion alternativa.
numero_original = 187.632587
numero_truncado = round(numero_original, 2)

print(numero_truncado)

#Solucion alternativa.
numero_original = 187.632587
numero_truncado = int(numero_original * 100) / 100

print(numero_truncado)


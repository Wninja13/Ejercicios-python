#Escribir un programa que permita ordenar una cadena de caracteres en orden alfabético ascendente. Para el caso la cadena es c='francia'. El resultado debe ser 'aacfinr'.
#Se utilizó un algoritmo de ordenamiento de burbuja. 
def ordenar_palabra(c): 
    #Convertir la palabra en una lista de letras. 
    lista_letras=list(c)
    #Obtener la longitud de la lista.
    longitud=len(lista_letras)
    #Bucle para ordenar las letras en orden ascendente.
    for i in range(longitud): 
        #Bucle para ordenar y reorganizar las letras.    
        for j in range(0,longitud-i-1): 
            #Comprar letras adyacentes. 
            if lista_letras[j]>lista_letras[j+1]: 
                #Si estan en orden incorrecto intercambiarlas.     
                lista_letras[j], lista_letras[j+1] = lista_letras[j+1], lista_letras[j]
    #Unir las letras ordenadas en una palabra            
    palabra_ordenada=''.join(lista_letras)
    return palabra_ordenada
#Palabra que queremos ordenar
c="Argentina"
#Llamar a la función para ordenar la palabra. 
palabra_ordenada=ordenar_palabra(c)
#Imprimir la palabra ordenada en orden ascendente. 
print('Palabra ordenada en orden ascendente:', palabra_ordenada)
    
    
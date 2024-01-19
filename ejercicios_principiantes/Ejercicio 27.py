# Escribir un programa que permita recuperar la extension de un archivo.
import os

def obtener_extension(nombre_archivo): 
    extension= os.path.splitext(nombre_archivo)[1]
    return extension

nombre_archivo = "documento.pdf"
extension = obtener_extension(nombre_archivo)
print("La extensión del archivo es:", extension)
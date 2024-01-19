# Escribir un programa que muestre la carpeta en al que se encuentra un programa en python. 
import os

# Obtener la ruta absoluta del directorio del script actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))

print("El script se encuentra en el directorio:", directorio_actual)

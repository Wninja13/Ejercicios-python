# escribir un programa que permita medir el tiempo de ejecución de un script. Si quieres puedes tomar como ejemplo para medir este script o cualquiera que gustes. 
#a=8 
#i=0

#for i in range(11):
    #print(f"{a} X {i}= {a*i}")

import time 
#Esto determina el inicio del tiempo o del contador.
inicio= time.time()
#Codigo que queremos medir. 
a=8 
i=0

for i in range(11):
    print(f"{a} X {i}= {a*i}")

#Fin del contador de tiempo. 
fin=time.time()

#Ahora calculamos el tiempo total de ejecucion. 
tiempo_ejecucion=fin-inicio
print('Tiempo de ejecucion:',tiempo_ejecucion,'segundos')
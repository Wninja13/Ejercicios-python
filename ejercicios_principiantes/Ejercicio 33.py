# Escribir un programa  cuya variable L contenga este contenido: [-6.5,-3,1,2,8,-3.6]. Luego, crear una lueva lista  usando comprension de lista con los numeros de L que son estrictamente mayores que 0 y mostrar el contenido de L1 en la consola. 

L=[-6.5,-3,1,2,8,-3.6]
L1=[x for x in L if x>0]
print('L1=',L1)
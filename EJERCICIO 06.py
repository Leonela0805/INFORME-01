# Un robot puede dar pasos de 1 o 2 metros
# Escriba un programa para numerar todas las maneras en que el robot camina n metros.

def pasos_robot(n):
    if n == 1 or n == 2:
        return n
    return pasos_robot(n-1)+pasos_robot(n-2)

p = int(input('Ingrese la cantidad de metros a recorrer: '))
for i in range (1, p+1):
    print (pasos_robot(i))
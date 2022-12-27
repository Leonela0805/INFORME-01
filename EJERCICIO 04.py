# Escriba un programa recursivo y otro no recursivo para calcular n!
# Compare los tiempos de ejecución

import time
def factorial_normal(n):
    r = 1
    i = 2

    while i<=n:
        r *= i
        i += 1
    return r
def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n* factorial_recursivo(n-1)
number= int(input('Ingrese número: '))
print ('El factorial de ', number, ' es: ',factorial_normal(number))
t1 = time.perf_counter()
t2=time.perf_counter()
print('El tiempo de ejecución es:',t2-t1)

print('El factorial recursivo de ', number, ' es: ',factorial_recursivo(number))
t1 = time.perf_counter()
t2=time.perf_counter()
print('El tiempo de ejecución es:',t2-t1)
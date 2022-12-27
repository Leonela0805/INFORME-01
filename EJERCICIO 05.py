# Escriba un programa recursivo y otro no recursivo para calcular la sucesión de Fibonacci
# Compare los tiempos de ejecución

import time
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        a, b = b, a+b
    return a

def fibonacci_recursivo(n):
    if n ==0 or n==1:
        return n
    else:
        return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)


number=int(input('Ingrese un número:'))
print('Fibonacci igual: ',fibonacci(number))
t1 = time.perf_counter()
t2=time.perf_counter()
print('El tiempo de ejecución es:',t2-t1)
print('Fibonacci recurisivo igual: ',fibonacci_recursivo(number)) 
t1 = time.perf_counter()
t2=time.perf_counter()
print('El tiempo de ejecución es:',t2-t1)
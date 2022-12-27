# Implemente la seleción por orden como un programa

import time
def seleccion_orden(a,n):
    for j in range (n):
        peq=a[j]
        pos = j
        for i in range(j+1,n):
            if a[i]<peq:
                peq = a[i]
                pos = i
        a[j],a[pos]=a[pos],a[j]
lista = list(input('Ingrese lista: '))
l = lista
t1 = time.perf_counter()
t2=time.perf_counter()
print(l,t2-t1)
l=lista
t1=time.perf_counter()
seleccion_orden(l,len(l))
t2 = time.perf_counter()
print(l,t2-t1)
# Implemente un programa para desordenar

import random
def desordenar(a,n):
    for i in range (n):
        r = random.randint (i,n-1)
        a[i],a[r]=a[r],a[i]

lista = list(input("ingrese lista: "))
desordenar(lista, len(lista))
print (lista)
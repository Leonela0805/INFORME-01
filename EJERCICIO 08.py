# Implemente un programa recursivo que calcule la potencia de un número elevado a otro.
# Sabenmos que 2n = 2n/2. 2n/2 donde n es par.
# 2n = 2(n-1)/2. 2(n-1)/2 si n es impar.

def potencia(a,b):
    if b == 1:
        return a
    else:
        if b % 2 == 0:
            p = potencia(a, int(b/a))
            return p*p
        else:
            return a * potencia(a, b-1)

n = int(input('Ingrese número: '))
m = int(input('Ingrese exponente: '))
print(potencia(n,m))
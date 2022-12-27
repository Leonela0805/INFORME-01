# Implementar un programa recursivo que sume dos número a +b.
# Considera que la suma a+b = a+1+1+...+1(b veces)

def suma_recursiva(a,b):
    if b == 0:
        return a
    else:
        return suma_recursiva(a, b-1)+1

n = int(input('Ingrese el primer número: '))
m = int(input('Ingrese el segundo número: '))
print(suma_recursiva(n,m))
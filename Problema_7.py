# Problema 7: Suma de números primos menores que 100

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):  # probamos todos los números menores que n
        if n % i == 0:
            return False
    return True

suma_primos = 0

for i in range(100):  # recorremos desde 0 hasta 99
    if es_primo(i):
        suma_primos = suma_primos + i  # sumamos los primos

print("La suma de todos los números primos menores que 100 es:", suma_primos)

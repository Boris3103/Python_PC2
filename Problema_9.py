# Problema 9: Números perfectos menores que 1000

for n in range(1, 1000):
    suma = 0
    for i in range(1, n):  # divisores menores que n
        if n % i == 0:
            suma = suma + i
    if suma == n:
        print("Número perfecto:", n)

# Problema 8: Serie de Fibonacci entre 0 y 50

a = 0
b = 1

print("Serie de Fibonacci entre 0 y 50:")

while a <= 50:
    print(a, end=" ")
    siguiente = a + b
    a = b
    b = siguiente

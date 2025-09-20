# Problema 10: Factorial
def factorial(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1
    return f

num = int(input("Ingrese un número entero no negativo: "))
print("El factorial de", num, "es:", factorial(num))

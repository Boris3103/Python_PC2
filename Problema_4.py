# Problema 4: Construir el patrón de asteriscos

n = 5  # altura máxima

# Parte creciente
for i in range(1, n + 1):
    print("* " * i)

# Parte decreciente
for i in range(n - 1, 0, -1):
    print("* " * i)

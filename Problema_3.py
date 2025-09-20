# Problema 3: Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700

# Lista para guardar los resultados
numeros = []

# Recorremos el rango
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        numeros.append(i)

print("Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:")
print(numeros)

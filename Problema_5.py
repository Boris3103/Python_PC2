# Problema 5: Contar pares e impares con entrada de usuario

numeros = []  # lista para guardar los números

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().lower()
    
    if respuesta == "si":
        num = int(input("Ingrese el número: "))
        numeros.append(num)
    elif respuesta == "no":
        break
    else:
        print("Por favor responda con SI o NO.")

# Contadores
pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\nNúmeros ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

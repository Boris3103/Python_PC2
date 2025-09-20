# Problema 11: Eliminar vocales de un texto

texto = input("Ingrese un texto: ")

vocales = "aeiouAEIOU"
resultado = ""

for letra in texto:
    if letra not in vocales:
        resultado = resultado + letra

print("Texto sin vocales:", resultado)

# Problema 2: Detectar tipo MIME según extensión

# Diccionario de extensiones y sus tipos MIME
tipos_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Pedir al usuario el nombre del archivo
archivo = input("Ingrese el nombre del archivo: ").strip().lower()

# Verificar la extensión
tipo = "application/octet-stream"  # valor por defecto
for ext, mime in tipos_mime.items():
    if archivo.endswith(ext):
        tipo = mime
        break

print("Tipo MIME:", tipo)

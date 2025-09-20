# Problema 12: Conversión de fechas a formato AAAA-MM-DD

meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

fecha = input("Ingrese una fecha (ej: 9/8/1636 o Septiembre 8, 1636): ").strip()

# Caso 1: formato con "/"
if "/" in fecha:
    m, d, a = fecha.split("/")
    m = int(m)
    d = int(d)
    a = int(a)
    print(f"{a:04}-{m:02}-{d:02}")

# Caso 2: formato con nombre del mes
else:
    partes = fecha.replace(",", "").split()
    mes_nombre = partes[0]
    d = int(partes[1])
    a = int(partes[2])
    m = meses.index(mes_nombre) + 1
    print(f"{a:04}-{m:02}-{d:02}")

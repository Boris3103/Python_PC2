# Problema 6: Registro de alumnos y sus calificaciones

alumnos = []  # lista para guardar los diccionarios

n = int(input("¿Cuántos alumnos desea registrar?: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    alumno = {
        "Alumno": nombre,
        "Notas": notas
    }
    alumnos.append(alumno)

print("\n Listado de alumnos y sus calificaciones:")
for a in alumnos:
    print(f"Alumno: {a['Alumno']}, Notas: {a['Notas']}")

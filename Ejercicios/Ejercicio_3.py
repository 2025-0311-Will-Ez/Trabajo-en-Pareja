asignaturas = ["Matemáticas" , "Física" , "Química" , "Historia" , "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    notas.append(nota)
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")
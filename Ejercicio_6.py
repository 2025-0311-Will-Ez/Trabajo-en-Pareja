asignaturas = ["Matemáticas" , "Física" , "Química" , "Historia" , "Lengua"]

suspendidas = []

for asignatura in asignaturas:
    nota = float(input(f"ingrese la nota de {asignatura}: "))

    if nota < 5:
        suspendidas.append(asignatura)

print("Las asignaturas que debes repetir son:")
print(suspendidas)
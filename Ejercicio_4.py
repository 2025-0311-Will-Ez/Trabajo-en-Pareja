numeros = input("Ingrese los números ganadores de la loteria, separados por comas: ")

numeros = [int(x) for x in numeros.split(",")]

numeros.sort()

print("Los números ganadores ordenados son:")
print(numeros)
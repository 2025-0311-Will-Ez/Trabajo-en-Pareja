import statistics

numeros = input("Ingrese una lista de números separados por comas: ")
numeros = [float(x) for x in numeros.split(",")]

media = statistics.mean(numeros)
desviacion_tipica = statistics.stdev(numeros)

print("La media es:", media)
print("La desviación típica es:", desviacion_tipica)
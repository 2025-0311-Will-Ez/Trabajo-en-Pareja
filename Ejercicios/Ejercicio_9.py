palabra = input("Ingrese una palabra: ")
contar = {}
for letra in palabra:
    if letra in contar:
        contar[letra] += 1
else:
    contar[letra] = 1
for letra, cantidad in contar.items():
    print(f"La letra '{letra}' aparece {cantidad} veces")

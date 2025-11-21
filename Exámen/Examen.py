def Capturar_Lista():
    lista = []      
    for i in range(10):
        num = int(input(f"Ingrese el número {i+1}: "))
        lista.append(num)
    return lista

lista_original = Capturar_Lista()

lista_mayores = [n for n in lista_original if n > 15]

print("Lista original:", lista_original)
print("Lista con Números mayores:", lista_mayores)
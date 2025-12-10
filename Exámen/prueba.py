def La_lista ():
    randy = []
    for i in range (10): 
        num = int(input(f"Ingrese el número {i+5}:"))
        randy.append(num)
    return randy

randy_original = La_lista ()

randy_mayores = [n for n in randy_original if n > 15]

print("Lista original:", randy_original)
print("Lista con números mayores:", randy_mayores)
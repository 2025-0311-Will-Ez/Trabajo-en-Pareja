abecedario = list("abcdefghijklmnopqrstuvwxyz")
for i in range(len(abecedario) - 1, -1, -1):
    if (i + 1) % 3 == 0:
        del abecedario[i]
print("".join(abecedario))
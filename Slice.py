


Cards = [
    "4242424242424242",
    "4000056655665556",
    "555555555554444",
    "378282246310005",
    "6011111111117",
]

for x in Cards:
    mastercard = ""
    if x.startswith("5"):
        mastercard = x[:5] + "xxxxx" + x[-4:]

    else:
        continue
    print(mastercard)
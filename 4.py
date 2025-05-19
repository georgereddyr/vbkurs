zeichenkette = ["fddfh3", "ggl23h33h45t", "werff34fref", "sdfsdfffff3333", "asdkhfbasjhdf"]

def laengste_zeichenkette(zeichenkette):
    laengste = ""
    laengste_zeichenkette = []
    for zeichenkette in zeichenkette:
        if len(zeichenkette) > len(laengste):
            laengste = zeichenkette
            laengste_zeichenkette = [zeichenkette]
        elif len(zeichenkette) == len(laengste):
            laengste_zeichenkette.append(zeichenkette)
    return laengste_zeichenkette   

laengste = laengste_zeichenkette(zeichenkette)

print(f"Die längste ist {laengste}")
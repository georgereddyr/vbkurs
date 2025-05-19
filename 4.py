zeichenkette = ["fddfh3", "ggl23h33h45t", "werff34fref", "sdfsdfffff333", "asdkhfbasjhdf"]

def laengste_zeichenketten(liste):
    max_laenge = max(len(s) for s in liste)
    return [s for s in liste if len(s) == max_laenge]

laengste = laengste_zeichenketten(zeichenkette)
print(f"Die längste Zeichenkette: {laengste}")
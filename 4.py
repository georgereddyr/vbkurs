zeichenkette = ["123", "1234", "12345", "1234566", "1234567"]
i = 0
maxLen = 0

while i < len(zeichenkette):
    if len(zeichenkette[i]) > maxLen:
        maxLen = len(zeichenkette[i])
    i += 1

i = 0 

laengste = []
while i < len(zeichenkette):
    if len(zeichenkette[i]) == maxLen:
        laengste.append(zeichenkette[i])
    i += 1

print(f"Die längste Zeichenkette: {laengste}")

#def laengste_zeichenketten(liste):
#    maxLen = maxLen(len(i) for i in liste)
#    return [i for i in liste if len(i) == maxLen]

#laengste = laengste_zeichenketten(zeichenkette)

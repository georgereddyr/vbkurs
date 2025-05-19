def dez_zu_bin(dezimalzahl):
    if dezimalzahl == 0:
        return "0"
    
    binaerzahl = ""
    while dezimalzahl > 0:
        binaerzahl = str(dezimalzahl % 2) + binaerzahl
        dezimalzahl //= 2
    return binaerzahl

dezimalzahl = input("Bitte geben Sie eine Dezimalzahl ein: ")
try:
    dezimalzahl = int(dezimalzahl)
    if dezimalzahl < 0:
        print("Bitte geben Sie eine positive Zahl ein")
    else:
        binaerzahl = dez_zu_bin(dezimalzahl)
        print(f"Die Binärdarstellung von {dezimalzahl} ist {binaerzahl}")
except ValueError:
    print("Das ist keine gültige Zahl")
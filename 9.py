def bin_zu_hex(binaerzahl):
    dezimalzahl = int(binaerzahl, 2) 
    hexadezimalzahl = hex(dezimalzahl)[2:].upper()  
    return hexadezimalzahl

binaerzahl = input("Bitte geben Sie eine binäre Zahl ein: ")
try:
    if all(bit in '01' for bit in binaerzahl):
        hexadezimalzahl = bin_zu_hex(binaerzahl)
        print(f"Die hexadezimale Darstellung von {binaerzahl} ist {hexadezimalzahl}")
    else:
        print("Das ist keine gültige binäre Zahl")
except ValueError:
    print("Das ist keine gültige Zahl")
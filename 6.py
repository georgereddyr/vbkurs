zahlen = input("1. Bitte geben Sie eine Liste von Zahlen ein: ").split()
summe = 0
summe_gerade = 0
summe_ungerade = 0

for zahl in zahlen:
    try:
        zahl = int(zahl)
        summe += zahl
        if zahl % 2 == 0:
            summe_gerade += zahl
        elif zahl % 2 != 0:
            summe_ungerade += zahl
    except ValueError:
        print(f"{zahl} ist keine gültige Zahl")
        
print(f"Die Summe ist {summe};\nDie Summe aller geraden Zahlen ist {summe_gerade};\nDie Summe aller ungeraden Zahlen ist {summe_ungerade}")

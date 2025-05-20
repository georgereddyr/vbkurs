def summe(eingabe):
    zahlen = eingabe.split()
    summe = summe_gerade = summe_ungerade = 0

    for z in zahlen:
        try:
            zahl = int(z)
            summe += zahl
            if zahl % 2 == 0:
                summe_gerade += zahl
            else:
                summe_ungerade += zahl
        except ValueError:
            print(f"'{z}' ist keine gültige Zahl.")

    return summe, summe_gerade, summe_ungerade

eingabe = input("Bitte geben Sie eine Liste von Zahlen ein: ")
gesamt, gerade, ungerade = summe(eingabe)

print(f"Gesamtsumme: {gesamt}\n Summe gerader Zahlen: {gerade} \n Summe ungerader Zahlen: {ungerade}" )

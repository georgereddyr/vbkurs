print("Spiel: ZAHLEN RATEN")

def zahlen_raten():
    print("Denk dir eine Zahl zwischen 1 und 1024 und gib sie ein.")
    print("Dann versuchst du, sie zu erraten!")

    gedachte_zahl = None
    while gedachte_zahl is None:
        eingabe = input("Geheime Zahl (wird nicht gezeigt): ")
        if eingabe.isdigit():
            gedachte_zahl = int(eingabe)
            if gedachte_zahl < 1 or gedachte_zahl > 1024:
                print("Nur Zahlen zwischen 1 und 1024")
                gedachte_zahl = None
        else:
            print("Bitte eine gültige Zahl eingeben")

    print("\n" * 55)
    print("Jetzt rate mal!")

    while True:
        tipp = input("Dein Tipp: ")
        if not tipp.isdigit():
            print("Bitte eine gültige Zahl eingeben")
            continue
        
        tipp = int(tipp)

        if tipp < 1 or tipp > 1024:
            print("Nur Zahlen zwischen 1 und 1024")
        elif tipp < gedachte_zahl:
            print("Zu niedrig!")
        elif tipp > gedachte_zahl:
            print("Zu hoch!")
        else:
            print("Treffer!")
            antwort = input("Willst du weiter spielen? (j/n) ")
            if antwort == "n":
                return
            elif antwort == "j":
                zahlen_raten()

zahlen_raten()

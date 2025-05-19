def caesar(text, verschiebung):
    def verschluesseln(char):
        if char.isalpha():
            basis = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - basis + verschiebung) % 26 + basis)
        return char

    return ''.join(verschluesseln(char) for char in text)

def eingabe_mit_validierung(prompt, validierungsfunktion):
    while True:
        try:
            wert = int(input(prompt))
            if validierungsfunktion(wert):
                return wert
            print("Ungültiger Wert.")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

def hauptmenue():
    modus = input("Möchten Sie verschlüsseln (v) oder entschlüsseln (e)? ").strip().lower()
    if modus not in {'v', 'e'}:
        print("Ungültige Auswahl")
        return

    text = input("Bitte geben Sie den Text ein: ")
    verschiebung = eingabe_mit_validierung("Bitte geben Sie die Verschiebung ein (1-25): ", lambda x: 1 <= x <= 25)

    if modus == 'e':
        verschiebung = -verschiebung

    ergebnis = caesar(text, verschiebung)
    print("Ergebnis:", ergebnis)

    hauptmenue()
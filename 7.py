def caesar_verschluesselung(text, verschiebung):
    verschluesselter_text = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            verschluesselter_char = chr((ord(char) - offset + verschiebung) % 26 + offset)
            verschluesselter_text += verschluesselter_char
        else:
            verschluesselter_text += char
    return verschluesselter_text

text = input("Bitte geben Sie den zu verschlüsselnden Text ein: ")
verschiebung = int(input("Bitte geben Sie die Verschiebung ein (1-25): "))

if verschiebung < 1 or verschiebung > 25:
    print("Die Verschiebung muss zwischen 1 und 25 liegen.")
else:
    verschluesselter_text = caesar_verschluesselung(text, verschiebung)
    print("Der verschlüsselte Text ist:", verschluesselter_text)
    
def caesar_entschluesselung(text, verschiebung):
    return caesar_verschluesselung(text, -verschiebung)

verschluesselter_text = input("Bitte geben Sie den zu entschlüsselnden Text ein: ")
verschiebung = int(input("Bitte geben Sie die Verschiebung ein (1-25): "))

if verschiebung < 1 or verschiebung > 25:
    print("Die Verschiebung muss zwischen 1 und 25 liegen.")
else:
    entschluesselter_text = caesar_entschluesselung(verschluesselter_text, verschiebung)
    print("Der entschlüsselte Text ist:", entschluesselter_text)
    
def dez_zu_bin(n):
    return bin(n)[2:]

def main():
    eingabe = input("Bitte geben Sie eine Dezimalzahl ein: ")
    try:
        zahl = int(eingabe)
        if zahl < 0:
            print("Bitte geben Sie eine positive Zahl ein.")
        else:
            binaer = dez_zu_bin(zahl)
            print(f"Die Binärdarstellung von {zahl} ist {binaer}")
    except ValueError:
        print("Das ist keine gültige Zahl.")
        
main()
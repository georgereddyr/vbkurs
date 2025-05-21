'''
Bank-Simulator
Im Zentrum des Bank-Simulators steht ein Text-Menu, über welches der Benutzer jeweils eine der
Funktionen Aussuchen kann. Die Funktionen sind:
1. Kunde Anlegen:
    1. Kundeninformationen sind:
        Vorname, Name, Adresse, Geburtsdatum, Beruf, voraussichtliches monatliches Einkommen,
        Vermögen (dictionary (key:'Vermögenstitel', value:'Wert')
2. Konto Anlegen:
    1. Kunde auswählen
    2. Kontoart: Sparbuch, Girokonto, Festgeld
    3. Zu allen Konten werden alle Kontobewegungen gespeichert: Datum, Betrag (+/-), Quelle/Ziel von
        Überweisungen
    4. jedes Konto hat eine Kontonummer
3. Buchung auf Konto durchführen
    1. Jahresabschluss durchführen
    2. Girokonto: monatliche Gebühren.
    3. Sparbuch: jährlich Zinsen
    (Kreditvergabe: Beispiel: ING-DIVA WebSite)
    4. Alle Daten laden/speichern ... ? Menüfunktion oder integriert in die einzelnen Bereiche?
'''
import os
import json
import datetime

alle_konten = []
alle_kunden = []
was = 0

#save data
def daten_speichern(dateiname, neuer_kunde):
    try:
        with open(dateiname, "r", encoding="utf-8") as f:
            daten = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        daten = []

    daten.append(neuer_kunde)

    with open(dateiname, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=4)

    print(f"Kunde wurde gespeichert")

#new customer
def kunde_anlegen():
    print("Neuen Kunden anlegen")
    
    vorname = input("Vorname: ")
    name = input("Name: ")
    adresse = input("Adresse: ")
    geburtsdatum = input("Geburtsdatum (TT-MM-JJJJ): ")
    
    try:
        einkommen = float(input("Monatliches Einkommen: "))
    except ValueError:
        einkommen = 0
        print("Ungültige Eingabe. Einkommen wird als 0 gesetzt")
    
    beruf = input("Beruf: ")
    
    vermoegen = {}
    while True:
        titel = input("Vermögenstitel: ")
        try:
            wert = float(input(f"Wert von {titel}: "))
            vermoegen[titel] = wert
        except ValueError:
            print("Ungültiger Wert")
        
        mehr = input("Noch ein Vermögenstitel? (j/n): ").lower()
        if mehr != "j":
            break

    kunde = {
        "Vorname": vorname,
        "Name": name,
        "Adresse": adresse,
        "Geburtsdatum": geburtsdatum,
        "Beruf": beruf,
        "Einkommen": einkommen,
        "Vermögen": vermoegen
    }

    alle_kunden.append(kunde)
    print(f"Kunde {vorname} {name} wurde angelegt.")
    daten_speichern("kunden.json", alle_kunden)
    return kunde

#new account
def konto_anlegen(kunde, kontoart, konto_numer, startguthaben=0, erstellungsdatum=None):
    if erstellungsdatum is None:
        erstellungsdatum = datetime.datetime.now().strftime("%d-%m-%Y")
    
    konto = {
        "konto_nummer": konto_numer,
        "besitzer": kunde,
        "kontoart": kontoart,
        "bewegungen": [{"datum": erstellungsdatum, "betrag": startguthaben, "info": "Eröffnung"}],
        "erstellt_am": erstellungsdatum
    }
    
    if startguthaben != 0:
        konto["bewegungen"].append({
            "datum": erstellt_am,
            "betrag": startguthaben,
            "info": "Startguthaben"
        })
    
    alle_konten.append(konto)
    
    print(f"Konto erfolgreich erstellt:\n"
          f"Nummer: {konto_numer}, Typ: {kontoart}, Inhaber: {kunde['Vorname']} {kunde['Name']}")

    return konto




    

def buchung():
    
    print()
    
kunde_anlegen()

'''
was = print(f" Kunde (1) oder Konto (2) anlegen: {was}")

if was == 1:
    kunde_anlegen()
elif was == 2:
    konto_anlegen()
'''
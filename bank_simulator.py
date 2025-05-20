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

kunde = {
    "Vorname": "",
    "Name": "",
    "Adresse": "",
    "Geburtsdatum": "",
    "Einkommen": 0,
    "Vermögen": {
        "Vermögentitel": ""
    }
    
}

konto = {
    "konto_numer": 0,
    "besitzer": kunde,
    "Jahresabschluss": "",
    
}


def konto_anlegen(kunde, kontoart, konto_numer):
    
    print()
    
    
def buchung(konto_numer):
    
    print()

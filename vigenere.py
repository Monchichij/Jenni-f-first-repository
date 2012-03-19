def vignere (klartext, schluessel):
    buchstaben_schluessel = {} #Zum Schluessel umwandeln
    anfang1 = ord("A") #fuer den Anfang der Schleife
    anfang2 = ord("a") #fuer den Anfang der Schleife
    for i in range(0, 26):
        buchstaben_schluessel [chr(anfang1+i)] = i
    for i in range (0, 26):
        buchstaben_schluessel [chr(anfang2+i)] = i
    # Mein Woerterbuch, wo alle Buchstaben und ihre Positionenverschiebung drin sind

    geheimtext = ""
    for i in range (len(klartext)):
        index2 = 1
        # Fuer spaeter, damit der Schluessel bei Leerzeichen uebersprungen werden kann
        schluessel_buchstabe_fuer_diese_runde = schluessel [index2 % len(schluessel)]
        #Buchstabe mit dem diese Runde verschluesselt wird
        # mit dem Rest von Index / Laenge Schluessel
        # -> wenn der Schluessel benutzt wurde, geht es von vorne los
        x_positionen = buchstaben_schluessel [schluessel_buchstabe_fuer_diese_runde]
        # Hier wird der Buchstabe in Positionen umgewandelt, um die verschoben wird
        zahl = ord (klartext [i]) + x_positionen
        # chr(zahl) ist der neue, verschluesselte Buchstabe
        if zahl > ord ("z") or ord ("Z")< zahl < ord("a"):
            zahl = zahl - 26
        if chr(zahl) in buchstaben_schluessel:
            geheimtext = geheimtext + chr (zahl)
            index2 +=1
        else:
            geheimtext = geheimtext + klartext[i]
    return geheimtext

klartext = raw_input("Gib den Text ein, der verschluesselt werden soll: ")
schluessel = raw_input("Gib den Schluessel ein, der benutzt werden soll: ")
print vignere (klartext, schluessel)

    
    

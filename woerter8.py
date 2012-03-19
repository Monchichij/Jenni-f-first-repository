def woerter (text, laenge):
    buchstaben = [ ]
    anfang1 = ord("A")
    anfang2 = ord("a")
    for i in range (0,26):
        buchstaben.append (chr(anfang1+i))
    for i in range (0,26):
        buchstaben.append (chr(anfang2+i))
    # Liste mit allen Buchstaben erstellen
    print buchstaben
    fund = {}
    # Woerterbuch fuer die gefunden Woerter
    gefunden = ""
    # String fuer das Wort gerade
    for i in range(len(text)-1):
        if len(gefunden)< laenge and text[i] in buchstaben:
            gefunden += text[i]
        elif len(gefunden) == laenge and text[i] not in buchstaben:
            fund [i] = gefunden
            gefunden = ""
        else:
            gefunden = ""
    return fund.values()

text = raw_input ("Aus welchem Text sollen Woerter herausgesucht werden(Bitte keine Umlaute): ")
laenge = input("Woerter, welcher Laenge sollen gesucht werden: ")
print woerter (text, laenge)
            

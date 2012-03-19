def vignere (klartext, schluessel):
    schlum = {} #Schluessel umwandeln
    schlum ['A'] = '0'
    schlum ['B'] = '1'
    schlum ['C'] = '2'
    schlum ['D'] = '3'
    schlum ['E'] = '4'
    schlum ['F'] = '5'
    schlum ['G'] = '6'
    schlum ['H'] = '7'
    schlum ['I'] = '8'
    schlum ['J'] = '9'
    schlum ['K'] = '10'
    schlum ['L'] = '11'
    schlum ['M'] = '12'
    schlum ['N'] = '13'
    schlum ['O'] = '14'
    schlum ['P'] = '15'
    schlum ['Q'] = '16'
    schlum ['R'] = '17'
    schlum ['S'] = '18'
    schlum ['T'] = '19'
    schlum ['U'] = '20'
    schlum ['V'] = '21'
    schlum ['W'] = '22'
    schlum ['X'] = '23'
    schlum ['Y'] = '24'
    schlum ['Z'] = '25'
    schlum ['a'] = '0'
    schlum ['b'] = '1'
    schlum ['c'] = '2'
    schlum ['d'] = '3'
    schlum ['e'] = '4'
    schlum ['f'] = '5'
    schlum ['g'] = '6'
    schlum ['h'] = '7'
    schlum ['i'] = '8'
    schlum ['j'] = '9'
    schlum ['k'] = '10'
    schlum ['l'] = '11'
    schlum ['m'] = '12'
    schlum ['n'] = '13'
    schlum ['o'] = '14'
    schlum ['p'] = '15'
    schlum ['q'] = '16'
    schlum ['r'] = '17'
    schlum ['s'] = '18'
    schlum ['t'] = '19'
    schlum ['u'] = '20'
    schlum ['v'] = '21'
    schlum ['w'] = '22'
    schlum ['x'] = '23'
    schlum ['y'] = '24'
    schlum ['z'] = '25'
    while len (schluessel) < len (klartext):
        if len (schluessel) + len (schluessel) < len (klartext):
            schluessel = schluessel + schluessel
        else:
            schluessel = schluessel + schluessel [0:len(klartext)-len (schluessel)]
    geheimtext = ""
    for i in range (len(klartext)):
        schl = schluessel [i] #Schluessel fuer den aktuellen Buchstaben
        schl2 = schlum [schl] #Schluessel in Nummer, aber String
        schl3 = int (schl2) # Schluesselnummer integer
        zahl = ord (klartext [i]) + schl3
        if zahl > ord ("z") or ord ("Z")< zahl < ord("a"):
            zahl = zahl - 26
        geheimtext = geheimtext + chr (zahl)
    return geheimtext

klartext = raw_input("Gib den Text ein, der verschluesselt werden soll: ")
schluessel = raw_input("Gib den Schluessel ein, der benutzt werden soll: ")
print vignere (klartext, schluessel)

    
    

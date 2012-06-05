# -*- coding: cp1252 -*-
from sys import argv

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())

# Ist es sinnvoller es ist in eine Zeile zu schreiben oder Variablen zu benutzen?
## wenn du variablen benutzt, kannst du die datei schließen
## ausserdem liest man und schriebt man nicht die ganze datei, sondern immer stücke..
## was ist wenn du enie 1gb datei hast?
### Wow, die Frage ist so genial gestellt, sie verwirrt mich erstmal selber. -.-"

# Muss ich .close() benutzen oder hier nicht? Wenn ja, wie benutze ich es hier?
# Mir faellt nur ein, die Datei nochmal zu oeffnen, aber das verfehlt sein Ziel ja.
## f = open(to_file, 'w') # erstellt ien dateiobjekt
## f.write(open(from_file).read())
## f.close() # das brauchst du aber nciht, weil python die datei selbst schliesst,
## sobald das objekt in keiner variable mehr verwendet wird.

#Kann ich auch zwei Dateien zusammenmatschen? Lohnt es sich, herauszufinden,
# wie das geht?
##
## was ist matschen?
### Matschen ist in diesem Zusammenhang  so was wie, ich nehm das aus der ersten Datei und
### fuege es einer schon vorhandenen Datei hinzu. Oder ich habe zwei Dateien und erstelle
### eine Kopie mit dem Inhalt von beiden?
#### wenn eine datei oeffenen magst, um was anzuhaengen, nutze open(name, 'a')

###Danke :)

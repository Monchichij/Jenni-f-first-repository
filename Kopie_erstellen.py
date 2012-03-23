# -*- coding: cp1252 -*-
from sys import argv

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())

# Ist es sinnvoller es ist in eine Zeile zu schreiben oder Variablen zu benutzen?
## wenn du variablen benutzt, kannst du die datei schließen
## ausserdem liest man und schriebt man nicht die ganze datei, sondern immer stücke..
## was ist wenn du enie 1gb datei hast?

# Muss ich .close() benutzen oder hier nicht? Wenn ja, wie benutze ich es hier?
# Mir faellt nur ein, die Datei nochmal zu oeffnen, aber das verfehlt sein Ziel ja.

#Kann ich auch zwei Dateien zusammenmatschen? Lohnt es sich, herauszufinden,
# wie das geht?
##
## was ist matschen?

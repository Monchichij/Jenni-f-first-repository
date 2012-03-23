from sys import argv

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())

# Ist es sinnvoller es ist in eine Zeile zu schreiben oder Variablen zu benutzen?

# Muss ich .close() benutzen oder hier nicht? Wenn ja, wie benutze ich es hier?
# Mir faellt nur ein, die Datei nochmal zu oeffnen, aber das verfehlt sein Ziel ja.

#Kann ich auch zwei Dateien zusammenmatschen? Lohnt es sich, herauszufinden,
# wie das geht?

import os

def irgendeine(a, b, c):
    print int(a) + int(b) + c   # int(), weil a und b aus der Datei Strings sind
    
if os.path.isfile('merke.txt'): # gibt es merke.txt?
    gemerkt = open('merke.txt')
    a = gemerkt.readline()      # a ist, was in der ersten Zeile steht - String!
    b = gemerkt.readline()      # b ist, was in der zweiten Zeile steht
else:
    a = input("> ")
    b = input("> ")
    merken = open('merke.txt', 'w')
    merken.write(str(a) + "\n") # a wird in die erste Zeile geschrieben
    merken.write(str(b))        # b wird in die zweite Zeile geschrieben
c = input ("> ")

irgendeine(a, b, c)



# Beispielsweise wuerde man in Python nicht testen, ob eine
# Datei existiert, bevor man sie zum Lesen oeffnet, sondern das
# Oeffnen versuchen und gegebenfalls die Ausnahme abfangen,
# die das Fehlen der Datei signalisiert.
# ... ? ? ?

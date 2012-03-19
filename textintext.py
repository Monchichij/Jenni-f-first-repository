
def finde (text, zufindentext):
    l = len (zufindentext) 
    anfang = 0
    such = text [ anfang : l]
    counter = len (text)
    while counter > 0:
        if such == zufindentext:
            return anfang
                       
        else:
            anfang += 1
            l += 1
            such = text [anfang : l]
            counter -= 1
    else:
        return "Nicht gefunden"

    

print "Lass uns Text in Text suchen!"
text = raw_input ("Gib bitte den zu untersuchenden Text ein: ")
zufindentext = raw_input  ("Gib bitte den Text ein, der gesucht werden soll: ")
wert = finde (text, zufindentext)
print "Das Wort beginnt auf der Position: ", wert
if wert == 0:
    print "Das war einfach! :)"
m = input ()
    


            

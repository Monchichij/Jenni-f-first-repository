#!/usr/bin/env python2
# -*- coding: cp1252 -*-
## die zeile drüber sorgt dafür, dass du es auch unter linux mit
## doppelklick auch ausführen kannst

## das modul sollte wie die klasse heißen, (Auto),
## wenn die klasse das wichtigste ist darin.

'''Auto

hier ist die modulbeschribung für meine klasse


'''

from Py_Input import integer_input




class Auto(object):
    '''
Klasse Auto, die man zum fahren benutzen kann.

'''
    def __init__(self, marke, farbe, sitze, speed, gang, fahrer):
        ## das print sollte in eine eigene funktion, denke ich
        ## ach hast du ja auch.. dann hier benutzen!
        ## die meisten fehler sind copy&paste fehler also
        ## oberste devise: copy&paste vermeiden!
        ## aus dieser devise sind
        ## schleifen und klassen entstanden

        ## gefällt mir!
        # Auto am Anfang
        self.marke = marke
        self.farbe = farbe
        self.sitze = sitze
        self.speed = speed
        self.gang = gang
        self.fahrer = fahrer

        ## das ist dasselbe wie
        ## print self.unser_auto()
        print Auto.unser_auto(self)
        ## schau mal nach unten und probier mal
        ## print self
        
    def umlackieren(self):
        neuefarbe = raw_input("In welcher Farbe soll das Auto lackiert werden?\n > ")
        self.farbe = neuefarbe
        
    def beschleunigen(self):
        ## input zu verwenden ist gefährlich, da man beliebigen
        ## programmtext einschleusen kann
        ## du solltest raw_input nehmen und dann testen
        ## z.B.
        ## while 1:
        ##     beschleunigung = raw_input(\
        ##                      "Wie stark soll beschleunigt werden?\n > ")
        ##     if beschleunigung.isalnum():
        ##         self.speed += int(beschleunigung)
        ##         break
        ##     print 'bitte nur zahlen eingeben'
        beschleunigung = integer_input(\
                             "Wie stark soll beschleunigt werden?\n > ")
        self.speed += int(beschleunigung)

    def bremsen(self):
        # input immer siehe beschleunigen
            bremsung = integer_input("Wie stark soll gebremst werden?\n > ")

    def schalten(self):
        schaltung = integer_input("In welchen Gang moechtest du schalten?\n > ")
        self.gang = schaltung

    def einsteigen(self):
        personen = integer_input("Wie viele Personen steigen ein?\n > ")
        self.fahrer += personen

    def aussteigen (self):
        personen = integer_input("Wie viele Personen steigen aus?\n > ")
        self.fahrer -= personen 
    
    def unser_auto(self):
        return """Unser Auto ist {1}, ein {0}, hat {2} Sitze,
                faehrt gerade {3} km/h im {4}.Gang mit {5} Personen im
                Auto.""".format(self.marke, self.farbe, self.sitze, self.speed, self.gang, self.fahrer)
        # Auto am Ende
        ## jetzt, wo du die methode das auto als string zurück gibt,
        ## kannst du sie auch __str__ nennen
    __str__ = unser_auto
        ## probier jetzt das mal aus:
        ## print self


if __name__ == '__main__':
    ## das ist für den fall, dass du dein auto nochmal importierst..
    ## dann soll das folgende nicht vom nutzer abgefragt werden sondern nur
    ## die klasse bereit gestellt werden.
    ## __name__ ist bei doppelklick auf die datei nur '__main__'
    ## solltest du im selben ordner import Klasse_Auto (je nach dateinamen)
    ## machen,
    ## dann ist __name__ der name nach dem import, ergo 'Klasse_Auto'
    
    marke = raw_input("Von welcher Marke ist unser Auto?\n > ")
    farbe = raw_input("Welche Farbe hat unser Auto?\n > ")
    sitze = integer_input("Wie viele Sitze hat unser Auto?\n > ")
    speed = integer_input("Mit welcher Geschwindigkeit fahren wir?\n > ")
    gang = integer_input("Welcher Gang ist eingelegt?\n > ")
    fahrer = integer_input("Wie viele Personen befinden sich im Auto?\n > ")

    Auto(marke, farbe, sitze, speed, gang, fahrer)
    ## gefällt mir!

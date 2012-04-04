class Auto(object):
    def __init__(self, marke, farbe, sitze, speed, gang, fahrer):
        print """Unser Auto ist {1}, ein {0}, hat {2} Sitze,
                faehrt gerade {3} km/h im {4}.Gang mit {5} Personen im
                Auto.""".format(marke, farbe, sitze, speed, gang, fahrer)
        # Auto am Anfang
        self.marke = marke
        self.farbe = farbe
        self.sitze = sitze
        self.speed = speed
        self.gang = gang
        self.fahrer = fahrer
        
    def umlackieren(self):
        neuefarbe = raw_input("In welcher Farbe soll das Auto lackiert werden?\n > ")
        self.farbe = neuefarbe
        
    def beschleunigen(self):
        beschleunigung = input("Wie stark soll beschleunigt werden?\n > ")
        self.speed += beschleunigung

    def bremsen(self):
        bremsung = input("Wie stark soll gebremst werden?\n > ")
        self.speed -= bremsung

    def schalten(self):
        schaltung = input("In welchen Gang moechtest du schalten?\n > ")
        self.gang = schaltung

    def einsteigen(self):
        personen = input("Wie viele Personen steigen ein?\n > ")
        self.fahrer += personen

    def aussteigen (self):
        personen = input("Wie viele Personen steigen aus?\n > ")
        self.fahrer -= personen
    
    
    def unser_auto(self):
        print """Unser Auto ist {1}, ein {0}, hat {2} Sitze,
                faehrt gerade {3} km/h im {4}.Gang mit {5} Personen im
                Auto.""".format(self.marke, self.farbe, self.sitze, self.speed, self.gang, self.fahrer)
        # Auto am Ende

marke = raw_input("Von welcher Marke ist unser Auto?\n > ")
farbe = raw_input("Welche Farbe hat unser Auto?\n > ")
sitze = input("Wie viele Sitze hat unser Auto?\n > ")
speed = input("Mit welcher Geschwindigkeit fahren wir?\n > ")
gang = input("Welcher Gang ist eingelegt?\n > ")
fahrer = input("Wie viele Personen befinden sich im Auto?\n > ")
Auto(marke, farbe, sitze, speed, gang, fahrer)

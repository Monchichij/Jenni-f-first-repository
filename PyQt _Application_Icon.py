import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    # Aehm... ja, cool, versteh ich nicht.

    def __init__(self):
        super(Example, self).__init__()
        # Auch nicht. Was ist super?
        # Warum bringen die Erklaerungen eigentlich nichts?
        # Und warum sieht das Ganze in der "Uebersetzung" anders aus?
        self.initUI()

    def initUI(self):
        # Aber initUi() wird doch da oben schon benutzt? ?

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        # Ich schaetze hier sollte man dann im Besitz von web.png sein?
        # Muss das im selben Ordner sein wie das Programm?

        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    # Das kenn ich schon, das haben wir dahinten auch gemacht...
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    

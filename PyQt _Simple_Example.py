import sys
from PyQt4 import QtGui

def main():

    app = QtGui.QApplication(sys.argv)
    # application-Objekt... aeh, ja? Weitere Ausfuehrungen bitte?
    # argv verstehe ich hoffentlich nach der Mail?

    w = QtGui.QWidget()
    # Widget... Blubber? Benutzeroberflaechenobjekte? Default-Konstruktor?
    # Elternklasse? Basisklasse? Hey, Fenster versteh ich. Da war die Erklaerung
    # mal so was von nicht hilfreich.
    # Aber das da macht uns ein Fenster, richtig?
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

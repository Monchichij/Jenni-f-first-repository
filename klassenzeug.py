

#### das macht jenni










##### das macht nicco



hans  = Student('Hans', 'Mayer')
assert hans.name == 'Hans'
assert hans.nachname == 'Mayer'

hans.set_alter(42)
assert hans.get_alter() == 42

hans.altern()
assert hans.get_alter() == 43

schule = Schule('Schule')

assert hans not in schule.schueler

schule.nehme_auf(hans)

assert hans in schule.schueler

##class X:
##    def __init__(self, xxxx):
##        ...
##
## a = X(xxxx)
## ///////////
## X
## X(xxxx)
## <X object> wird erstellt
## __init__(<X object>, xxxx) wird aufgerufen
## ... wird abgearbeitet
## <X object> wird in a gespiechert

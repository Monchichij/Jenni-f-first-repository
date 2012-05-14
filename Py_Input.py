def integer_input(text):
    while True:
        user_input = raw_input(text)
        try:
            zahl = int(user_input)
        except ValueError:
            print "Please enter only numbers."
        else:
            return zahl
        
            

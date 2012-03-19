def wort (text):
    buchst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W","X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    such1 = text[i]
    such2 = text[i+1]
    such3 = text[i+2]
    such4 = text[i+3]
    such5 = text[i+4]
    fund = []
    while i < len(text)-5:
        if such1 not in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 not in buchst:
            fund.append (text[i+1:i+4])                
        i+=1
        such1 = text[i]
        such2 = text[i+1]
        such3 = text[i+2]
        such4 = text[i+3]
        such5 = text[i+4]        
    print fund

text = raw_input ("Aus welchem Text sollen Woerter herausgesucht werden: ")

wort (text)


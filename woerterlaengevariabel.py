def wort3 (text):
    buchst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W","X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    such1 = text[i]
    such2 = text[i+1]
    such3 = text[i+2]
    such4 = text[i+3]
    such5 = text[i+4]
    fund = {}
    while i ==0:
        if such1 in buchst and such2 in buchst and such3 in buchst and such4 not in buchst:
            fund [i] = text[i:i+3]
        break
    while i < len(text)-5:
        if such1 not in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 not in buchst:
            fund [i] = text[i+1:i+4]                
        i+=1
        such1 = text[i]
        such2 = text[i+1]
        such3 = text[i+2]
        such4 = text[i+3]
        such5 = text[i+4]
    while i == len(text)-5:
        if such2 not in buchst and such3 in buchst and such4 in buchst and such5 in buchst:
            fund [i] = text[i+2:i+5]
        break
    return fund.values()

def wort4 (text):
    buchst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W","X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    such1 = text[i]
    such2 = text[i+1]
    such3 = text[i+2]
    such4 = text[i+3]
    such5 = text[i+4]
    such6 = text[i+5]
    fund = {}
    while i ==0:
        if such1 in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 not in buchst:
            fund [i] = text[i:i+4]
        break
    while i < len(text)-6:
        if such1 not in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 not in buchst:
            fund [i] = text[i+1:i+5]                
        i+=1
        such1 = text[i]
        such2 = text[i+1]
        such3 = text[i+2]
        such4 = text[i+3]
        such5 = text[i+4]
        such6 = text[i+5]
    while i == len(text)-6:
        if such2 not in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst:
            fund [i] = text[i+2:i+6]
        break
    return fund.values()

def wort5 (text):
    buchst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W","X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    such1 = text[i]
    such2 = text[i+1]
    such3 = text[i+2]
    such4 = text[i+3]
    such5 = text[i+4]
    such6 = text[i+5]
    such7 = text[i+6]
    fund = {}
    while i ==0:
        if such1 in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 not in buchst:
            fund [i] = text[i:i+5]
        break
    while i < len(text)-7:
        if such1 not in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 not in buchst:
            fund [i] = text[i+1:i+6]                
        i+=1
        such1 = text[i]
        such2 = text[i+1]
        such3 = text[i+2]
        such4 = text[i+3]
        such5 = text[i+4]
        such6 = text[i+5]
        such7 = text[i+6]
    while i == len(text)-7:
        if such2 not in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 in buchst:
            fund [i] = text[i+2:i+7]
        break
    return fund.values()

def wort6 (text):
    buchst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W","X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    such1 = text[i]
    such2 = text[i+1]
    such3 = text[i+2]
    such4 = text[i+3]
    such5 = text[i+4]
    such6 = text[i+5]
    such7 = text[i+6]
    such8 = text[i+7]
    fund = {}
    while i ==0:
        if such1 in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 not in buchst:
            fund [i] = text[i:i+6]
        break
    while i < len(text)-8:
        if such1 not in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 in buchst and such8 not in buchst:
            fund [i] = text[i+1:i+7]                
        i+=1
        such1 = text[i]
        such2 = text[i+1]
        such3 = text[i+2]
        such4 = text[i+3]
        such5 = text[i+4]
        such6 = text[i+5]
        such7 = text[i+6]
        such8 = text[i+7]
    while i == len(text)-7:
        if such2 not in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 and such8 in buchst:
            fund [i] = text[i+2:i+8]
        break
    return fund.values()

def wort7 (text):
    buchst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W","X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    such1 = text[i]
    such2 = text[i+1]
    such3 = text[i+2]
    such4 = text[i+3]
    such5 = text[i+4]
    such6 = text[i+5]
    such7 = text[i+6]
    such8 = text[i+7]
    such9 = text[i+8]
    fund = {}
    while i ==0:
        if such1 in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 in buchst and such8 not in buchst:
            fund [i] = text[i:i+7]
        break
    while i < len(text)-9:
        if such1 not in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 in buchst and such8 in buchst and such9 not in buchst:
            fund [i] = text[i+1:i+8]                
        i+=1
        such1 = text[i]
        such2 = text[i+1]
        such3 = text[i+2]
        such4 = text[i+3]
        such5 = text[i+4]
        such6 = text[i+5]
        such7 = text[i+6]
        such8 = text[i+7]
        such9 = text[i+8]
    while i == len(text)-9:
        if such2 not in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 and such8 in buchst and such9 in buchst:
            fund [i] = text[i+2:i+9]
        break
    return fund.values()

def wort8 (text):
    buchst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W","X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    such1 = text[i]
    such2 = text[i+1]
    such3 = text[i+2]
    such4 = text[i+3]
    such5 = text[i+4]
    such6 = text[i+5]
    such7 = text[i+6]
    such8 = text[i+7]
    such9 = text[i+8]
    such10 = text[i+9]
    fund = {}
    while i ==0:
        if such1 in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 in buchst and such8 in buchst and such9not in buchst:
            fund [i] = text[i:i+8]
        break
    while i < len(text)-10:
        if such1 not in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 in buchst and such8 in buchst and such9 in buchst and such10 not in buchst:
            fund [i] = text[i+1:i+9]                
        i+=1
        such1 = text[i]
        such2 = text[i+1]
        such3 = text[i+2]
        such4 = text[i+3]
        such5 = text[i+4]
        such6 = text[i+5]
        such7 = text[i+6]
        such8 = text[i+7]
        such9 = text[i+8]
        such10 = text[i+9]
    while i == len(text)-10:
        if such2 not in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 and such8 in buchst and such9 in buchst and such10 in buchst:
            fund [i] = text[i+2:i+10]
        break
    return fund.values()

def wort9 (text):
    buchst = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W","X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    such1 = text[i]
    such2 = text[i+1]
    such3 = text[i+2]
    such4 = text[i+3]
    such5 = text[i+4]
    such6 = text[i+5]
    such7 = text[i+6]
    such8 = text[i+7]
    such9 = text[i+8]
    such10 = text[i+9]
    such11 = text[i+10]
    fund = {}
    while i ==0:
        if such1 in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 in buchst and such8 in buchst and such9 in buchst and such10 not in buchst:
            fund [i] = text[i:i+9]
        break
    while i < len(text)-11:
        if such1 not in buchst and such2 in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 in buchst and such8 in buchst and such9 in buchst and such10 in buchst and such11 not in buchst:
            fund [i] = text[i+1:i+10]                
        i+=1
        such1 = text[i]
        such2 = text[i+1]
        such3 = text[i+2]
        such4 = text[i+3]
        such5 = text[i+4]
        such6 = text[i+5]
        such7 = text[i+6]
        such8 = text[i+7]
        such9 = text[i+8]
        such10 = text[i+9]
        such11 = text[i+10]
    while i == len(text)-11:
        if such2 not in buchst and such3 in buchst and such4 in buchst and such5 in buchst and such6 in buchst and such7 and such8 in buchst and such9 in buchst and such10 in buchst and such11 in buchst:
            fund [i] = text[i+2:i+11]
        break
    return fund.values()

text = raw_input ("Aus welchem Text sollen Woerter herausgesucht werden: ")
laenge = input("Woerter, welcher Laenge sollen gesucht werden: ")
if laenge == 3:
    print wort3(text)
if laenge == 4:
    print wort4(text)
if laenge == 5:
    print wort5(text)
if laenge == 6:
    print wort6(text)
if laenge == 7:
    print wort7(text)
if laenge == 8:
    print wort8(text)
if laenge == 9:
    print wort9(text)

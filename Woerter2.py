buchst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
text = "wenn ich jetzt diesen satz tippe, wie teilst du ihn in worte?"
i = 0
such = text[i]
counter = 0
while counter< len(text):
    if such in buchst:
        counter +=1
        i+=1
        such = text[i]
    else:
        print text[0:i]
        counter2 = counter
        i+=1
        such = text [i]
        counter = len (text)+1
while counter2< len(text):
    if such in buchst:
        counter2 +=1
        i+=1
        such = text[i]
    else:
        print text[0:i]
        counter3 = counter2
        i+=1
        such = text [i]
        counter2 = len (text)+1
while counter3< len(text):
    if such in buchst:
        counter3 +=1
        i+=1
        such = text[i]
    else:
        print text[0:i]
        counter3 = len (text)+1
    

def function(lm, c):
    liste = []
    for i in range(len(lm)):
        length = len(lm[i])
        word = lm[i]
        if word[length-1] == c:
            liste.append(word)
    return liste

lm = ["hello", "new", "hoho"]
c = "o"
print(function(lm, c))
        

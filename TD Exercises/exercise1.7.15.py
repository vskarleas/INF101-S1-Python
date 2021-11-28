def function(lm, c):
    liste = []
    for i in range(len(lm)):
        length = len(lm[i])
        word = lm[i]
        if word[length-1] == c:
            liste.append(word)
    return liste


def function2(lm, c):
    liste = []
    for i in range(len(lm)):
        alpha = lm[i]
        if alpha[0] == c:
            liste.append(alpha)
    return liste

def function4(lm, c):
    liste = []
    for i in range(len(lm)):
        if c in lm[i]:
            liste.append(lm[i])
    return liste

def function5(lm, c, n):
    liste = []
    for i in range(len(lm)):
        while n >0:
            word = list(lm[i])
            for k in range(len(word)):
                if c == word[k]:
                    word.pop(k)
                    n = n - 1
        if c in word:
            liste.append(lm[i])
        elif n == 0:
            liste.append(lm[i])
    return liste


def function3(lm, c, a):
    #True for beginning letter
    #False for last letter
    liste = []
    if a == True:
        liste = function2(lm, c)
    else:
        liste = function(lm, c)
    
    return liste

lm = ["hello", "new", "hoho"]
c = "a"
a= False
n = 2
print(function5(lm, c, n))


        

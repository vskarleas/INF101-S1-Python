def function(text):
    cad = text.split()
    liste=[]
    for i in range(len(cad)):
        caf = len(cad[i])
        liste.append(caf)
    return liste

def function2(text):
    cad = text.split()
    liste=[]
    somme = 0
    for i in range(len(cad)):
        caf = len(cad[i])
        liste.append(caf)
        somme = somme + caf
    return somme

def plus_long(text):
    kart = text.split()
    klm = function(text)
    longeur = max(klm)
    
    laf = klm.index(longeur)
    raf = kart[laf]
    return raf

def plus_long2(text, moy):
    kart = text.split()
    klm = function(text)
    for j in range(len(kart)):
        if len(kart[j]) > moy:
            longeur = kart[j]
    return longeur

def moyenne(text):
    trg = text.split()
    trt = len(trg)
    somme = function2(text)
    moy = somme / trt
    live = plus_long2(text, moy)
    return live

def voyelles(mot):
    lowercase = mot.lower()
    counter = 0
    for i in lowercase:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            counter = counter +1
    return counter

def plus_voyelles(text):
    olp = text.split()
    previous = 0
    for r in range(len(olp)):
        mot = olp[r]
        wrt = voyelles(mot)
        if wrt > previous:
            previous = wrt
            identify = olp[r]
    return identify


text = "hei hol hix holla hohohohohohohoho"
print(plus_voyelles(text))
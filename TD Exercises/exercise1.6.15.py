def decalage(x, n):
    liste1=[]
    #In this list we will create the alphabet so that we 
    #are sure that it's not a notation and this way is 
    #accepted on the exams as well
    for i in range(ord("a"), ord("z")+1):
        liste1.append(chr(i))

    liste2=[]
    for k in range(ord("A"), ord("Z")+1):
        liste2.append(chr(k))

    if (x not in liste1) and (x not in liste2):
        return x

    #We are using the modulo so that we can move on in the "list of letters masculins or not".
    elif ord(x)+n>ord("z"):
        return (ord(x)+n)%ord("z")+ord("a")

    elif ord(x)+n>ord("Z"):
        return (ord(x)+n)%ord("Z")+ord("A")

def decal_list(l, n):
    l2=[]
    for i in l:
        x = i #Maybe l[i]
        l2.append(decalage(x, n))
    return l2

def list_to_string(li):
    mot = ''
    for i in range(len(li)):
        mot = li[i]
    return mot


#Main programm
h = ""
while h != "stop":
    h = str(input("Add the word: "))
    n = int(input())
    l = list.h
    li = decal_list(l, n)
    print(list_to_string(li))






def list_to_string2(listing2):
    character = "a"
    for i in range(0, len(listing2)):
        for k in range(i, i+1):
            character = ord("a")+1
            character = chr(character)
            l = k
            if listing2[k] <= character:
                listing2.append(listing2[k])
            else:
                character = listing2[k]
                listing2.append(character)
    return listing2

    
listing2 = ['a', 'z', 'c', 'b']
print(list_to_string(listing2))
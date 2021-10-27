maliste=[1,3,9,6,4]

print(maliste)
a = maliste[2]
b = maliste[0]
c = maliste[4]
d = maliste[-1]
#Donne error e = maliste[7]

i = 0
while i <len(maliste):
    element= maliste[i]
    print("indice ", i, "contient: ", element)
    i = i +1
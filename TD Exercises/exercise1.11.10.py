def compteNotes(dictionary, name):
    for key, value in dictionary.items():
        if name == key:
            return len(value)

def meileurNote(dictionary, name):
    for key, value in dictionary.items():
        if name == key:
            best = max(value)
    return best

def meileurSemestre(dictionary):
    newDictionary = {}
    data = []
    notes = []
    for key, value in dictionary.items():
        final = 0
        for i in range(len(value)):
            final = final + value[i]
        length = len(value)
        moy = final/length
        newDictionary[key]= [moy, length]

    for key2, value2 in newDictionary.items():
        data.append(key2)
        notes.append(value2)

    first = notes[0][0]
    tests = notes[0][1]
    for i in range(1, len(data)):
        if first < notes[i][0] and notes[0][1]>=tests:
            first = notes[i][0]
            name = data[i]
            tests = notes[0][1]
    return name, first

#Other way to do it:
def maileurSemestre2(dictionary):
    nom = ""
    moy = 0
    for e in dictionary:
        m = sum(dictionary[e]/len(dictionary[e]))
        if m >moy:
            moy = m
            nom = e
    return nom, moy
    

def plusAbsent(dictionary):
    absent = 730
    name = ""
    for k in dictionary: #k represents the different keys of the dictionary (key = student name)
        if len(dictionary[k]) < absent:
            absent = len(dictionary[k])
            name = k
    return name, absent

#Number 4
d = {1:[1,2,3], 2:[1,4,9], 'autres':{3:None, 4:[1,16], 5:[1,32]}}
print(d)
d.update(d['autres'].items())
del d['autres']
print(d)
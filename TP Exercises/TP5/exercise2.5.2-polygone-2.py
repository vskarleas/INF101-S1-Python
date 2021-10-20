from turtle import *
from math import *

def diametre(nb_cotes, cote):
    diametre = cote/(sin(pi/nb_cotes))
    return diametre

nb_cotes = 6
cote = 20
print(diametre(nb_cotes, cote))

import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
#This help as to insert the well known linespace!!!
from math import *


def calculerDelta(a,b,c):
    return b*b-4*a*c

def resoudreEquationSecondDegre(a,b,c):
    delta = calculerDelta(a,b,c)
    if delta > 0:
      racineDeDelta= sqrt(delta)
      retour = [(-b-racineDeDelta)/(2*a),(-b+racineDeDelta)/(2*a)]
    elif delta < 0:
      retour = []  #liste vide
    else:
      retour = [-b/(2*a)] #liste d'un seul élément
    return retour
# Function two numbers with different signes
def signe_different(x, y):
    if x > 0 and y < 0:
        return True
    elif x < 0 and y > 0:
        return True
    elif (x == 0) or (y == 0):
        return False
    else:
        return False

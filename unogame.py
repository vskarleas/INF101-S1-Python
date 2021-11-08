#Uno Game Program

def cardsDeck():
    colors = ['green', 'red', 'blue', 'yellow']
    options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    multioptions = ['+4', 'joker']
    deck = []
    for i in range(len(colors)):
        for repater in range(2):
            for k in range(len(options)):
                result = options[k]+" "+colors[i]
                deck.append(result)
        deck.append('0'+" "+colors[i])
    for h in range(len(multioptions)):
        deck.append(multioptions[h])
    return deck

print(cardsDeck())
dictionary = {"a":"alpha", "d":"dog"}
for x, y in dictionary.items():
    repeat = 0
    for i in range(len(y)):
        if x == y[i]:
            repeat = repeat + 1
    print(x, "appears in word", y, repeat, "times")
    
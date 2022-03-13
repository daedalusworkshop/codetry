# a fast train rushing
# a   fast      train           rushing
def hermes(words,multiplier) :
    x = 0
    list = words.split()
    for i in list:
        print(list[i], end = " " * x)
        x += 1

hermes("a fast train rushing", 3)
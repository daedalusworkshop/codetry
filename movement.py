# a fast train rushing
# a   fast      train           rushing
def hermes(words) :
    x = 0
    y = 0
    for len in words:
        if words[x] == " ":
            y = x
        else:
            print(words[x])
            if y == x:
                print(words[0:x])
            else:
                x += 1

hermes("a fast train rushing")
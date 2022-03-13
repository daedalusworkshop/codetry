# a fast train rushing
# a   fast      train           rushing
def hermes(words,multiplier) :
    x = 0
    list = words.split()
    for i in range(len(list)) :
        print(list[i], end = " " * multiplier)
        multiplier = multiplier * 2
hermes("a fast train rushing", 3)
# hermes(input("phrase: "), input("multiplier: "))
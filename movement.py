# a fast train rushing
# a   fast      train           rushing
def hermes(words,multiplier) :
    list = words.split()
    int(multiplier)
    for i in range(len(list)) :
        print(list[i], end = " " * multiplier)
        multiplier *= 2
hermes(input("phrase: "), int(input("multiplier: ")))
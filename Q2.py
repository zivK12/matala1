# Q2
def revword(word):
    revWord = word[::-1].lower()
    return revWord


def countword(file):
    word = file.readline().rstrip()
    counter = 1
    for line in file:
        l = line.rstrip().split()
        for i in l:
            i = revword(i)
            if i == word:
                counter += 1
    return counter


file = open('C:/Users/Ziv1/Desktop/python/DataSets/matala1.txt')

# print(countword(file))

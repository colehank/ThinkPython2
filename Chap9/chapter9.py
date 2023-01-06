fin=open('words.txt')
def findlinetwenty(x):
    for line in x:
        if len(line)>20:
            print(line)
findlinetwenty(fin)

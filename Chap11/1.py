import random

words = open('words.txt')


def is_inWords(s):
    d = dict()
    for i in words:
        val = random.random()
        d[i] = val
    print(s in d)
        
is_inWords('apple\n')#后面是换行符


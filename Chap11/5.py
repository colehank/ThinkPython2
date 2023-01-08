from rotate import rotate_word
import random


words = open('words.txt')

def WordsDict():
    d = dict()
    for i in words:
        word = i.strip().lower()#.strip删除多余符（换行符），.lower全部转为小写
        d[word] = random.random()
    return d        

    
def rotate(word):
    D = WordsDict()
    for i in range(1, 26):
        rororo = rotate_word(word, i)
        if rororo in D:
            return(word, rororo)
        
        
print(rotate('yay'))
      
        
        


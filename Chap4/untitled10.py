#9.1
fin = open ('words.txt')
def words(fin):
    for word in fin :
        if len(word)>20:
            print(word)
print(words(fin))

#9.2
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
        return False
    
#9.3 
def avoids(word,forbidden):
    for letter in word:
        if letter in forbidden:
            return False
        return True
print(avoids('apple', 'ech'))


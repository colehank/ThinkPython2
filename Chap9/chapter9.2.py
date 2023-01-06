fin=open('words.txt')
def has_no_e(x):
    for line in x:
        if line == 'e':
            return False
    return True
print(has_no_e(fin))
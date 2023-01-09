from prac_4 import import_word_list
from prac_1_2 import import_book



def not_in_list(mybook, mywords):
    return list(set(mybook) - set(mywords))

book = import_book("69746-0.txt")
words= import_word_list('words.txt')   
             
not_in_list(book,words)

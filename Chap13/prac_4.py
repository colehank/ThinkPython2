#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
打印所有在书上而不在单词库中的单词
"""

from prac_1_2 import init,import_book



def import_word_list(filename):
    
    with open(filename, "r") as f:
        bl = list()
        for line in f:
            bl.append(line.strip())#建立一个列表，包括了单词表所有的单词
        return bl



def not_in_list(book_words, word_list):#在书不在单词库

    not_in = list()

    for word in book_words:
        if word not in word_list:
            not_in.append(word)

    return not_in











mybook = import_book("69746-0.txt")
mywords= import_word_list('words.txt')


word_list = init(mybook)#
not_in = not_in_list(mybook, mywords)


for word in not_in:
    print(word)



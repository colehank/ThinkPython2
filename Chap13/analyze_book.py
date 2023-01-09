"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string
import random



def ski_beg(filename):
    book = open(filename,'r')#r只读
    for line in book:
        if line.startswith('*END*THE'):
            break
        return line.startswith('*END*THE')

print(ski_beg('158-0.txt'))



def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    #制作统计
    hist = {}
    fp = open(filename)

    if skip_header:
        ski_beg(filename)

    for line in fp:
        process_line(line, hist)
    return hist


def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1


def most_common(hist):
    """Makes a list of the key-value pairs from a histogram and
    sorts them in descending order by frequency."""
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency
    num: number of words to print
    """
    t = most_common(hist)
    print ('The most common words are:')
    for freq, word in t[:num]:
        print( word, '\t', freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)


if __name__ == '__main__':
    hist = process_file('emma.txt', skip_header=True)
    print ('Total number of words:', total_words(hist))
    print ('Number of different words:', different_words(hist))

    t = most_common(hist)
    print ('The most common words are:')
    for freq, word in t[0:20]:
        print( word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print ("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print( word,)

    print ("\n\nHere are some random words from the book")
    for i in range(100):
        print (random_word(hist),)


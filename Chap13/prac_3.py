from prac_1_2 import init,import_book,word_frequency

def top_20(word_freq):
    fr = list()
    for word, freq in word_freq.items():
        fr.append((freq, word))
    fr.sort(reverse=True)
    #以上都是字典那一章，反转键值对的操作

    mf = list()
    for (freq, word) in fr:
        mf.append(word)
    return mf[:20]#那么，只要到第20项就好了



filename = '/Users/harrischeung/Documents/GitHub/think_python/think_python/Chap13'
mybook = import_book("69746-0.txt")

word_list = init(mybook)
word_freq = word_frequency(word_list)

top_words = top_20(word_freq)

for word in top_20(word_freq):
    print(word)



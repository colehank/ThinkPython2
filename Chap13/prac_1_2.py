#1

import string

def init(w):
    del_del = w.translate(w.maketrans('', '',string.punctuation))
    out = del_del.lower().strip().split()#小写，删除两头空格，分割符为无
    return out#返回的是一个列表

#string.punctuation：是一个常量，表示所有的标点符号
#方法：str.maketrans(str1, str2，str3)：制作str1转为str2的转换表(映射)，str3是要删除的。
#string.translate:(table)str.maketrans的转换表传给string.translate打组合拳，来改变原str
#.strip（）：从两头开始，删除参数设置的字符


#print(init('  bo#ok%b!!c  '))



#2
def import_book(filename):#
    with open(filename, "r") as f:
    #有了这个with open，就不用每次打开了还关闭，文件的操作只在句内有效
        book_string = str()
        for i in range(46):
            next(f)#next()：接收一个迭代器，返回迭代器的下一项，迭到46行结束
        for line in f:#在第47行开始循环
            book_string += line#去头的书在此，遍历进book_string
        return book_string#注意，返回的是字符串哦



#parse_book(text)


def word_frequency(word_list):
#返回一个以单词为key，频率为val的字典，第11章有此函数histogram
    hist = dict()
    for word in word_list:
        hist[word] = hist.get(word, 0) + 1
    return hist


#####################
#### RUN PROGRAM ####
#####################
filename = '/Users/harrischeung/Documents/GitHub/think_python/think_python/Chap13'
mybook = import_book("69746-0.txt")

word_list = init(mybook)#返回book所有单词组成的列表
word_freq = word_frequency(word_list)

print("total words: {}".format(len(word_list)))
print(word_freq)
print("different words: {}".format(len(word_freq)))












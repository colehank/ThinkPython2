import shelve


from anagram_sets import all_anagrams, signature


def store_anagrams(filename, anagram_map):
    #filename是建立的数据库的名字，anagram_map把字符串映射到异序词的字典
    #函数：把异序字母保存在shelf里的字典
    shelf = shelve.open(filename, 'c')
    #shelve：持久保持对象的方法，.open获取一个shelve对象，操作完.open后写入文件
    #第二个参数，c：新建读写，n：总是创建空文件夹后读写，w：读写存在文件，r：只读存在文件
    for word, word_list in anagram_map.items():
        shelf[word] = word_list
    shelf.close()
       


def read_anagrams(filename, word):
    #在数据库shelf寻找word并返回这个word的异序词的序列
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []
        
anagram_map = all_anagrams('words.txt')

store_anagrams('word.txt', anagram_map)#把word.txt写入数据库
read_anagrams('word.txt', 'reverse')#执行查找异序词的功能

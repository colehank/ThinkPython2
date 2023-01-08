def rank(s):#是s的字母按顺序排列
    t = list(s)#将字符串转为列表
    t = sorted(t)#序列方法：排序
    t = ''.join(t)
    #在每个项目间的分割符，不加的话就是列表格式，按逗号分开了,加这个输出是str
    return t#返回的是字符串

#print(rank('banana'))


def dict_anagrams(filename):
    #返回文件中所有单词对应的的异序词序列的字典d
    d = dict()
    for i in open(filename):
        #关键：因为所有异序词经过排序都是相同的，根据这一点就可以找到他们
        word = i.strip().lower()#初始化单词
        t = rank(word)#t就是排序过的单词        
        if t not in d:
            d.setdefault(t,[]).append(word)
            #如果d中还没有t，那就建立一个key（t），val是[]而紧接着添加word
        else:
            d[t].append(word)
            #如果t已经写入d了，那键值就把新word写入这个键值
    return d

#print(dict_anagrams('words.txt'))




def rank_anagrams(d):
    #把所有的异序词序列按照序列大小将序排列，遍历异序词字典
    t = []
    for i in d.values():#读取异序词序列字典，遍历它的键值
        if len(i) > 1:#这里长度对应键值（一个序列）的元素个数，大于1才是有效的异序词
            t.append((len(i), i))#把元组（长度，异序词列表）写入列表
    t.sort()#一样的，排序按照元组第一个元素排序
    for i in t:#遍历这个列表
        print(i)


"""
RUN SELECTION Plz
"""
d = dict_anagrams('words.txt')
rank_anagrams(d)

"""
RUN SELECTION Plz
"""

#%%
def amp(d, n):
    #只选择有n个字母的单词，返回这种单词与对应异序词序列的字典
    dic = dict()
    for word, anagrams in d.items():
        if len(word) == n:
            dic[word] = anagrams
    return dic

"""
RUN SELECTION Plz
"""
d = dict_anagrams('words.txt')
amp(d,8)

"""
RUN SELECTION Plz
"""
#思路：调换两个字母的位置就成为另外一个单词，首先可以判定这俩词就是异序词，条件是两词在每个位置上的差异为2
#先定义两个词在每个位置上的差异，然后在异序词按着这样的差异遍历

from b_2 import dict_anagrams#导入异序词库

def word_diff (w1,w2):
    #说明两单词在相同位置上不同的字母的数量
    diff = 0#定义两单词的差异值
    if len(w1) == len(w2):#长度不一样就不会是异序词了
        d = zip(w1,w2)#创建两词字字对应的字典
        for l,v in d:#l，是w1的字，v是w2的字
            if l != v:
                diff += 1#在同一位置不等一次便加一
        return diff
    else:
        return False

#print(word_diff('abuu', 'cbud'))#理想的就是diff为2，有两个字母位置不等

def find_pair(d):
    #找到异序词库中，符合条件的单词
    for i in d.values():#在异序词键值中
        for w1 in i:
            for w2 in i:
                if w1 <w2 and word_diff(w1, w2) == 2:
                    print(w1,w2)
                    

d = dict_anagrams('words.txt')
find_pair(d)
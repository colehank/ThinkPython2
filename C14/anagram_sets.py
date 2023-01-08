from __future__ import print_function, division


def signature(s):#是s的字母按顺序排列
    """Returns the signature of this string.

    Signature is a string that contains all of the letters in order.

    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)#将字符串转为列表
    t = sorted(t)#序列方法：排序
    t = ''.join(t)#在每个项目间的分割符，这里每个字母都是一个项目，所以‘’指间隔为0
    return t#返回的是字符串

def all_anagrams(filename):
    #返回文件中所有单词对应的的异序词序列的字典d
    d = {}
    for line in open(filename):
        word = line.strip().lower()#初始化单词
        t = signature(word)#t就是排序过的单词

        # TODO: rewrite using defaultdict
        
        if t not in d:
            d.setdefault(t,[]).append(word)
            #如果d中还没有t，那就建立一个key（t），val是[]而紧接着添加word
        else:
            d[t].append(word)
            #如果t已经写入d了，那键值就把新word写入这个键值
    return d


def print_anagram_sets(d):
    """Prints the anagram sets in d.
    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    #把所有的异序词序列按照序列大小将序排列，打印（项目数，[异序词序列]）
    
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)


def filter_length(d, n):
    #只选择有n个字母的单词，返回一个单词与对应异序词序列的新映射
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    anagram_map = all_anagrams('words.txt')
    print_anagram_sets_in_order(anagram_map)

    eight_letters = filter_length(anagram_map, 8)
    print_anagram_sets_in_order(eight_letters)
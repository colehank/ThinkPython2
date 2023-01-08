def make_word_dict():
    #老朋友，读取文件
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None
        #按题目提示，加上这些字母
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

#make_word_dict()


memo = {}
memo[''] = ['']


def children(word, word_dict):
#返回word的所有删减字母仍能存在的单词，列表（孩子们）
    res = []
    for i in range(len(word)):#以单词长度循环
        child = word[:i] + word[i+1:]#每次循环去掉一个字母
        if child in word_dict:#若去掉一个字母还在单词库
            res.append(child)#添加到孩子们里
    return res

#word_dict = make_word_dict()
#children('sprite', word_dict)


def is_reducible(word, word_dict):
    #这是备忘录做法
    if word in memo:
        return memo[word]
    # 检查所有孩子并制作一个她们的列表，主要是存入备忘录
    res = []
    for child in children(word, word_dict):#对于孩子们
        if is_reducible(child, word_dict):
            res.append(child)#把孩子们的每个元素都写入res
    # memoize and return the result
    memo[word] = res#每个孩子都是一个元素，存入备忘录列表
    return res

#word_dict = make_word_dict()
#is_reducible('i', word_dict)



def all_reducible(word_dict):
 #检查字母库所有字母，如果可减，都装入本函数 
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)#遍历整个字母库，可以是孩子的都是t
        if t != []:#附加个条件，t不能是空列表
            res.append(word)#将合格的单词写入函数
    return res

#word_dict = make_word_dict()
#all_reducible(word_dict)


def print_trail(word):
    #打印可以减到0的单词，
    if len(word) == 0:#t不断传入is_re,is_re会不断缩减它，直到它长度为0，即''
        return#长度为哦、0，即成了''后退出
    print(word, end=' ')#打印出每次is_re缩减过程中输出的列表，调整项目间距离为一个空格' ' 
    t = is_reducible(word, word_dict)#t值是输入的单词对应的列表
    print_trail(t[0])#相当于用这句循环了，t也就是is_reducible每次值返回一个项的列表，t[0]就是他自己

#print_trail('restarting')

def print_longest_words(word_dict):
    #找到最长的可减词并打印
    words = all_reducible(word_dict)
    t = []
    for word in words:#对于所有可以减到头的字母
        t.append((len(word), word))#写入t
    t.sort(reverse=True)#t按照长度，逆向排序
    for _, word in t[0:5]:#_啥意思？
        print_trail(word)#从字母的原始状态到只剩一个字母的状态打印处理
        print('\n')#每循环打印一次，换个行



word_dict = make_word_dict()
print_longest_words(word_dict)











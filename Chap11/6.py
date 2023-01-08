def read_dictionary(filename='c06d'):
    d = dict()
    fin = open(filename)
    for line in fin:
        # skip over the comments
        if line[0] == '#': continue
        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron
    return d
#####################以上发音字典提供##########################################
        
words = open('words.txt')
mapping = read_dictionary(filename='c06d')


def WordsDict():
    d = dict()
    for i in words:
        word = i.strip().lower()#.strip删除多余符（换行符），.lower全部转为小写
        d[word] = word
    return d      

D = WordsDict()

def pronounce(a, b, mapping):#检查a,b的发音是否一样，mapping：单词和发音的映射
    if a not in mapping or b not in mapping:
        return False#如果a或b不在字典里就False
    return mapping[a] == mapping[b]#返回的是布尔值！


def check_word(word, D, phonetic):
#检查a，b是否具有Car Talk字谜的要求
    word_1 = word[1:] #单词去掉第个一个字母
    if word_1 not in D:#筛选仍然成立为字母的
        return False
    if not pronounce(word, word_1, mapping):#筛选读音相同的
        return False
    word2 = word[0] + word[2:]#去掉第二个字母
    if word2 not in D:
        return False
    if not pronounce(word, word2, mapping):#筛选发音相同的
        return False
    else:
        return True





def checkit():
    for word in D:
        if check_word(word, D, mapping):
            print(word, word[1:], word[0] + word[2:])

checkit()
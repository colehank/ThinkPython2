#%% 1
"""
RUN SELECTION Plz
"""
def nested_sum(t):
    total = 0
    for numbers in t:
        total +=sum(numbers)#题目中是网络列表，所以还得sum子列表的元素
    return total

t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)

#%% 2

"""
RUN SELECTION Plz
"""
def cumsum(t):
    empty = []
    total = 0
    for i in t:#不可照搬题1，因为1返回总的一个值，因此此处应该再循环内就记录下来每次的值
        total = i + total
        empty.append(total)
    return empty  

      
t = [1, 2, 3]
cumsum(t)

#%%3
"""
RUN SELECTION Plz
"""
def middle(t):
    empty=[]
    t= t[1:-1]
    empty.append(t)#对比答案写的太麻烦了，不必设新列表再传入，直接原来的t修改后就指向新值了
    return t   

    
t = [1, 2, 3, 4]
middle(t)

#%% 4
def chop(t):
    del t[0]
    del t[-1]
        #不返回值
        
#%% 5
def is_sorted(t):
    return t==t.sorted()#bool运算默认返回bool值的

#%% 6
#sorted()是一个函数，可以排序列表

def is_anagram(a,b):
    l_a = a.sort()
    l_b = b.sort()
    for i in l_a:
        for v in l_b:
            return i == v

#%% 7 
def has_duplicates(t):
    sorted(t)#出错，这样没有将排序的值赋予给任何对象
    for i in t:#出错，这样循环到最后一位就超出范围了
        if t[i]==t[i+1]:
            return True
        return False
t=[1,3,1,4]
has_duplicates(t)
#出错，应该排序来解决元素不相邻但相等的情况

def has_duplicates(t):
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
        else:
            return False

"""
RUN SELECTION Plz
"""
t=[1,3,1,4]
has_duplicates(t)

#%% 8
#weki：生日悖论：人数过23人便有50%的概率有两人同天生日
#在23个（1，365）的随机数中间，有两个数相等的概率近似50%
import random

def has_duplicates(t):
    t.sort()
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

def random_Day(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):#在*次模拟中，
        t = random_Day(num_students)#t是每次模拟的学生数量
        if has_duplicates(t):#如果循环中的某次模拟存在相同的生日
            count += 1#记述，+1
    return count


def Birthday_paradox():
    num_students = 23
    num_simulations = 1000#当模拟次数为1000时，事件数为495，概率近似了50%
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)
    

"""
RUN SELECTION Plz
"""
Birthday_paradox()

#%% 9
words = open('words.txt')


def function_1():
    t = []
    for i in words:
        x = i.strip()#x是words中去掉空格的word
        t.append(x)
    return t
"""
RUN SELECTION Plz
"""
function_1()


words = open('words.txt')

def function_2():
    t = []
    for i in words:
        x = i.strip()
        t += [x]
    return t
"""
RUN SELECTION Plz
"""
function_2()


#%% 10,11
"""
RUN SELECTION Plz
"""
words = open('words.txt')

def function_1():#生成word.txt的字符串
    t = []
    for i in words:
        x = i.strip()
        t.append(x)
    return t

def in_bisect(word_list, word):#返回word是否存在于在word_list
    if len(word_list) == 0:
        return False
    
    i = len(word_list) // 2
    if word_list[i] == word:
        return True
    if word_list[i] > word:
        #这个分半法，就是一直把列表分半（地板除余），直到目标值在这一半的中间，报告True
        return in_bisect(word_list[:i], word)
    else:
        return in_bisect(word_list[i+1:], word)
    
def palindrome_is_exist(word_list,word):#看列表单词的回文是否存在于列表
   rev_word = word[::-1]
   return in_bisect(word_list, rev_word)


def is_palindrome():#列出是回文词的字符串
    word_list = function_1()
    for word in word_list:
        if palindrome_is_exist(word_list,word):
            print(word)

is_palindrome()

#%% 12
"""
RUN SELECTION Plz
"""
words = open('words.txt')

def thelock(word_list,word):
    evens=word[::2]#[start:end:length],此处为全部范围，每两步取一值，即偶数项
    odds=word[1::2]#从1项开始到结束，即奇数项
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
    #在看是否奇数项和偶数项都相反的字母存在

def lock_n(word_list, word, n):#检查一个字母是否包含n个互锁字
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True

word_list = function_1()

def locklock():    
    for word in word_list:
        if thelock(word_list, word):
            print(word)        
#locklock()
def locklocklock():
    for word in word_list:
        if lock_n(word_list, word, 3):
            print(word)
locklocklock()


    
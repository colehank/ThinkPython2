"泛化过程：string——list——dictionary"

'1_mapping'
#字典是一种映射，从键——键值的映射
eng2sp = dict()#创建空字典
eng2sp#{}

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}#建立映射
eng2sp#{'one': 'uno', 'three': 'tres', 'two': 'dos'}
#注：字典的顺序是不固定的，因为是按照硬盘的特性存储

eng2sp['two']#dos
#'eng2sp['fouor']##KeyErro:不存在这个键'

len(eng2sp)#返回字典的 键值对 数目

'one' in eng2sp #in：判断 键 是否存在字典

vals = eng2sp.values() #.values：判断 键值 是否存在于字典
'uno' in vals#True




"2_键要是可哈希的"
#哈希：接受一个（任何类型）值返回一个整数（哈希值），字典使用哈希值存储和查找键对
#key在确立时，python将会哈希它并储存在某位置，如果改变键盘，会重新哈希，位置 也就改变了，和原来值的对应也没有了
#所以，键必须要是可哈希的

##############################################################################

"计数器"


def histogram(s):#频次的集合
    d = dict()
    for c in s:
        if c not in d:#如果c没有在字典中
            d[c] = 1 #字典中创建一个项，key为c，value为1
        else:
            d[c] += 1#如果c在字典中，对d[c]累加
    return d#返回的字典中，key为str，value为其数量
h = histogram('brontosaurus')
h

print(eng2sp.get('one',7))#字典.get（key，默认值）：获得字典键的键值，若不存在键，返回默认值

def histogram_better(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0)+1#键值等于项目返回的值+1，若不存在，默认值为0+1就新建，若存在，键值+1便计数
    return d

h = histogram_better('brontosaurus')
h

"逆向查找"

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionary')#这里raise是一个报错功能，在出错是会显示后面的LookupError
 
  
k = reverse_lookup(h, 2)
k

##############################################################################

"字典和列表"
#列表可以理解为字典里的键值

def invert_dict(d):#这是一个逆转字典的函数
    inverse = dict()#创建新字典
    for key in d:#循环d的键
        val = d[key]#定义d的键值
        if val not in inverse:#若d的键值不在新建的字典里
            inverse[val] = [key]#d的这个键就赋值给新字典的键值
        else:#若键值在新字典
            inverse[val].append(key)#新字典的这个键值添加d的键
    return inverse#返回新字典
#这就把原先一个键——多个键值的映射反转，原先的键值作为键，相同的作为一项，原先的键作为键值

hist = histogram('parrot')
inverse = invert_dict(hist)
inverse
##############################################################################
"备忘录"

def fibonacci (n): 
    if n == 0: 
        return 0 
    elif n == 1: 
        return 1 
    else: 
        return fibonacci (n-1) + fibonacci (n-2)

#若函数参数增大，运算时间也会变长，用备忘录可以缓解

known = {0:0, 1:1}#设定fibonaci的已知条件，备忘录
def fibonacci_faster(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res#将备忘录不断扩展，添加计算过的值
    return res


##############################################################################
"全局变量global与局部变量local"

a = True
def sample1():
    if a:
        print('running sample1')#所有函数内部均可以使用全局变量
        



been_called = False

def example2():
    been_called = True
    #这里在函数内想要改变全局变量，输出显示全局变量不会改变，因为它只在函数内复制了全局变量

def example3():
    global been_called
    been_called = True
    #这里在函数内调用全局变量本体而不是复制
    

"如果全局变量可修改，就无需global，如字典可以添加元素"

known = {0:0, 1:1}
def example4():
    known[2] = 1
    
#但是如果要给全局变量重新赋值就要global了    
def example5():
    global known
    known = dict()











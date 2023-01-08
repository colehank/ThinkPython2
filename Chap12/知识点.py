"元组不可修改"
#元组与列表十分类似，区别在于不可修改

t = 1,'2','c',4#加括号也行t = （1,'2','c',4）
t = 'a',#单个值必须加个逗号
t = (1)#这不是元组,而是赋值了

t = tuple()#会建立空白元组
t = tuple('apple')#若是任何序列(str,list,tuple)，会把序列元素拆开储存

print(t)
print(t[0:3])

#元组要改只能替换
t1 = ('A',) + t[1:]
print(t1)

print((0,1,2)<(0,1,1))#这种关系运算（从第一个开始比较，若相等延后）适用于所有序列




"元组建立并赋值"
a,b,c, = 1,2,3

addr = 'monty@python.org'
uname,domain = addr.split('@')

print(uname)
print(domain)


"元组做返回值"
t = divmod(7,3)#计算7/3的商和余，返回两参数2，1，赋值给t直接存为元组

quot,rem = divmod(7, 3)
print(quot)
print(rem)

def min_max(t):
    return min(t),max(t)

t = 100,2
print(min_max(t))




"元组参数长度可变"
#方法：用*开头做形参名的函数就可以接收任意多个参数到一个元组中
'聚集元素'
def printall(*args):#args约定俗成
    print(args)
printall(1,3,'2')

'分散元素'
#方法：用*开头做形参名的函数就可以把元组中的元素分散为多个参数
t = 7,3
#divmod(t):报错，因为该函数必须接收两个参数
divmod(*t)


"列表和元组"
s = 'ab'
t = [1,2,3]
print(zip(s,t))#返回的是zip对象

for i in zip(s, t):
    print(i)

zip#是一种迭代器，可以迭代整个序列的对象，类似列表但不能如列表不能索引
#如果要如列表索引等功能，可以转化为列表
print(list(zip(s,t)))#列表的元素是诸多元组，长度由最短的一项绝对

"赋值给元组列表"
x = list(zip(s,t))
for a,b in x:
    print(b,a)
    
#应用：用元组序列遍历两个以上的序列
def has_match(t1, t2):
    #如果存在i使得t1[i]和t2[i]一样反真
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

#内建函数enumerate：遍历一个序列及其索引
for i,x in enumerate('abc'):#i,x这里将元组拆开了，返回的是两个字符
    print(i, x)
#返回一个枚举对象，从0开始对应第一个元素

for i in enumerate('abc'):#i是一个整体，返回的是元组
    print (i)
                   
    
"字典与元组"
#.item方法，会把字典里的键值对以元组的形式返回出来
d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)#返回的是一个迭代器，迭代键值对

#结合zip和dict可以建立字典
d = dict(zip('abc', range(3)))
print(d)

    
'用元组作为字典的key'
last = 'Zhang','Wa'
first = 'Guohao','Haha'
number = 2045,1024
D = {}

D[last, first] = number#D接受的是一个元组

for last,first in D:
    print(first,last,D[last,first])


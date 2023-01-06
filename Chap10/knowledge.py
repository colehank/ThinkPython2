'列表的方法'

t = ['a', 'b', 'c']
#1 .append//添加元素
t.append('d')
t#['a', 'b', 'c', 'd']
#2 .extend//添加列表
t2 = ['d', 'e']
t.extend(t2)
t#['a', 'b', 'c', 'd', 'e']
#3 .sort 按ASCLL码排序
t.sort()#['a', 'b', 'c']

'列表的三种重要方法'
##reduce功能，将诸多元素缩减为单值
def add_all(t):
    total = 0
    for x in t:
        total += x#+=是更新变量的简写，即 total = total +x 
    return total

t=[1,2,3]
add_all(t)

sum(t)#内建函数，就等于ad_all了

##map功能，将某一函数应用到列表的每一个元素
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())#将res的所有元素应用于s.capialize
    return res

#fitter功能，过滤需要的内容
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():#如果列表里有大写字母
            res.append(s)#加入列表
    return res

############################################################################

'删除元素'

t = ['a', 'b', 'c']
#1 pop 删除原列表的函数，并返回删除的元素
x = t.pop(1)#如果不指明位置，删除最后一个元素（-1）
t#['a', 'c']
x#'b'
#2 del 直接删除
del t[1]
t#['a', 'c']
#3 remove 删除元素而不知道位置
t.remove('b')
t#['a', 'c']
##4 切片与索引删除
t=['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
t=['a', 'f']

############################################################################

'列表和字符串的转换'
#list 将字符串转为列表
s = 'spam'
t = list(s)
t#['s', 'p', 'a', 'm']

#spilt 把字符串分为单词
s = 'pining for the fjords'
t = s.split()#可传入形参，为界定符，默认为空格
t#['pining', 'for', 'the', 'fjords']

#join 把列表转为字符串
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '#此处设置界定符，join必须先设置界定福=符
s = delimiter.join(t)
s#'pining for the fjords'

############################################################################

'对象'
#在字符串中，python只相同的值只建立一个对象（推测）
a = 'banana'
b = 'banana'
a is b#True//此处在检验a，b是否指向一个对象（虽然值二者相同）

#在列表中，python不同对象可以值相同（推测）
a = [1, 2, 3]
b = [1, 2, 3]
a is b#False//值相同，但对象不同

'别名'
#相同值不同对象的两个列表，互为彼此的别名，并且，其中一个的改变会同步到另一个列表
a = [1, 2, 3]
a = b
b[0] = 42
a#[42, 2, 3]

'列表参数'
#列表里，.append是在原基础增加元素，+是生成两个列表，原对象不变
#**对象与值举例
t4 = [1, 2, 3]

def delete_head(t):
    del t[0]  

def bad_delete_head(t):
    t = t[1:]   #此处，将新值赋予了列表t，而原列表不发生改变
    
def tail(t):
    return t[1:]  #作为上一种的替代，不赋予新值，直接改了原列表

############################################################################

'1.大多数列表方法都返回空值，与字符串相反（返回新字符串，原字符串不变）'
'2.选择一一种方法坚持使用'
'3. 尽量做备份，避免用别名'


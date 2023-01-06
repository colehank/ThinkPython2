#7.1 重新赋值
a=3
b=a
a=5
print(b)#赋值需要谨慎，被赋值不会随原先值改变而改变。


#7.2 更新变量（更新赋值的方法）
x=0#先初始化x即赋予一个值，否则x=x+1报错，因为python先算等号右边
x=x+1#递增
x=x-1#递减


#7.3 while语句
def countdown(n):
    while n>0:
        print(n)
        n=n-1
    print('Blastoff')

countdown(4)

##while语句的执行流程
#1 判断条件真假，
#2 若假，退出while，运行接下来的，
#3 若真，运行while循环主体，而后返回while的第一步

#余除，指分子除以分母后，输出余数，python运算符：%

#while循环举例
def sequence(n): 
    while n != 1: 
        print(n) 
        if n % 2 == 0: # n is even 
           n=n/2
        else: # n is odd 
            n = n*3 + 1

sequence(3)#此函数的n时而增时而减，难以确定函数最终停止（n=1），无人证明此函数适用于所有的n


#用迭代重写递归
def countdown_1(n):#原迭代函数
    if n <=0:
        print('blastoff')
    else:
        print(n)
        countdown_1(n - 1)
        
def countdown_2(n):
    while n> 0:
        print(n)
        n=n-1#递减
    print('blastoff')

#7,4 break语句跳出循环

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)#此处print与break没有关系，仍然在while循环中，所以并非break后才print，是每次循环都print，同理，break属于if函数
print('Done!')

#7.5 平方根
#牛顿法求平方根：
y=(x+a/x)/2
a=4#取一个任意值
x=3
print(y)
#下面用y的值再运算一遍
x=y
y=(x+a/x)/2
print(y)
#不断重复x=y，y带入计算，就会得到无限近似2的值，以下用while循环表示
def sqrt_x(x):
    while True: 
        print(x) 
        y = (x + a/x) / 2 
        if y == x: #此处是比较浮点数，不能说想等，浮点数应该用内置函数abs计算，即if abs(y-x)<epsilon: break
            break 
        x=y
sqrt_x(4)
#改进后：
epsilon=0.0000001
a=4
def sqrt_x(x):
    while True: 
        print(x) 
        y = (x + a/x) / 2 
        if abs(y-x)<epsilon:#此处epsilon为决定精读的一个值，如0.0000001
            break 
        x=y
sqrt_x(4)


#7.6 算法Algorithm；设计算法：计算机科学的核心
#算法：解决一类问题的通用过程

#7.7 调试
#书上说明了一个小技巧，在代码的中间或者容易出错的地方print或其他方式验证一下，若报错则前面的都有问题。
    
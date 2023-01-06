#5.1 
import time 
X= time.time()
Day= str(X // (24*60*60))
Hour=str((X %(24*60*60)) // (60*60))
mini=str(((X %(24*60*60)) % (60*60)) // 60)
second=str(((X %(24*60*60)) % (60*60)) % 60)


def time_1():
    print('纪元到现在经过了' + Day + '天' + Hour + '小时' + mini + '分钟' + second + '秒')
    
#5.2.1
def check_fermat(a,b,c,n):
    if n>2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    elif n<=2:
            print('请输入大于2的数字')
    else:
        print('No, that doesn’t work.')

#5.2.2

def checkit():
    a=int(input('请输入整数a:'))
    b=int(input('请输入整数b:'))
    c=int(input('请输入整数c:'))
    n=int(input('请输入大于的2的数字n:'))
    check_fermat(a,b,c,n)
   
checkit()

#5.3
def is_triangle(a,b,c):
    if a>b+c or b>a+c or c>a+b:
        print('No')
    else:
        print('Yes')

def tryme():
    a=int(input('请输入a边: \n'))
    b=int(input('请输入b边: \n'))
    c=int(input('请输入c边: \n'))
    is_triangle(a,b,c)
    
tryme()

#5.4
def recurse(n, s): 
    if n == 0: 
        print(s) 
    else: 
        recurse (n-1, n+s ) 

#recurse函数意将n逐次递减1，同时，s在每次n递减之前都会与其相加，当n递减为0是输出s值。

recurse(-1, 0)#当n为-1，n值无法递减值0，因此会进入无限递归，直到python递归的最大深度。

#5.5

import turtle
bob = turtle.Turtle ()
bob.speed(0)

def draw(t,length,n):
    if n == 0:
        return
    angle=50
    t.fd(length*n)
    t.lt (angle)
    draw(t,length,n-1)#n=n-1,那么length=length*n，分支长度就会不断变短
    t.rt(2*angle)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)

draw(bob, 10, 5)
turtle . mainloop ()
#每次都有两个分支，分支的长度越来越短，函数被调用了两次，

#5.6
import turtle
bob=turtle.Turtle()
bob.speed(0)

def koch(t,x):
    if x>=3:
        koch(t,x/3)
        t.lt(60)
        koch(t,x/3)
        t.rt(120)
        koch(t,x/3)
        t.lt(60)
        koch(t,x/3)
    else:
        t.fd(x)
x=200

koch(bob,x)
turtle . mainloop ()
    
#5.7
def snowflake(t,x):
    for i in range (3):
        koch(t,x)
        bob.rt(120)
        
snowflake(bob,100)
        
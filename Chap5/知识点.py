#！/usr/bin/env python3

#5.1整余除
x=100
y=60
print(x // y)
print(x % y)

#5.2布尔表达式
print(x==y)
#布尔的特殊值：True,False

#5.3三种逻辑运算符
print(not(x!=y))
print(x == y or x > y)
print(x == y and x > y)
 
#5.4 有条件执行
if x>0:
    print('x是正数')
    
if x<0:
    pass #先留个位置，需要时再写
    
#5.5二选一
if x%2 == 0:
    print('x是偶数')
else:
    print('x是奇数')
    
#5.6 链式条件
if x > y:
    print('x比y大')
elif x<y:
    print('x比y小')
else:
    print('x等于y')

#5.7镶嵌条件
if x > y:
    print('x比y大')
else:
    if x<y:
        print('x比y小')
    else:
        print('x等于y')

#5.8递归
def countdown(n): 
    if n <= 0: 
        print('Blastoff!') 
    else: 
        print(n) 
        countdown (n-1)#调用自己的过程为递归
        
countdown(3)
    
def print_n(s, n): 
    if n <= 0: 
        return 
    print(s) 
    print_n (s, n-1)
    
print_n('zgh',3 )

#5.9 堆栈图
def do_n(s,n):
    if n <= 0:
        return 
    else:
        print(s,n)
        do_n(s,n-1)
        if n == 0:
            return
    
do_n('bnux',4)

#5.10 无限递归:指函数被无限调用

#5.11 输入
import random   # 导入随机数random模板
# 定义变量
top = 100
bottom = 1
 # 记录输入次数
i = 1      

random_num = random.randint(1, 100)  # 随机产生一个1-100之间的数
print('答案：', random_num)
 
print('=====欢迎来到猜数字游戏=====')
while True:
    # 带提示字符串拼接输入
    num = float(input('请输入一个' + str(bottom) + '-' + str(top) + '的整数：'))
    if num > int(num) or num < 0:
        print('请输入正整数！！！')
        continue
    # 结束游戏
    if num == 0:
        print(' ========退出游戏========')
        break
    # 根据输入的数字给予提示
    if random_num == num:
        print('恭喜您猜对了')
        break
    if random_num > num:
        print('您猜的数字小了')
        bottom = int(num)
    if random_num < num:
        print('您猜的数字大了')
        top = int(num)
    # 提示语
    if i % 5 == 0:
        print('不是吧！您太水了！')
    i += 1

        

    
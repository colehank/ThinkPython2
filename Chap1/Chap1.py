#%%1.1
#1、2 语法错误
#3 对于'++'，数字前的+指的是这个数字的正负，即1++1指1+（+1）=2，2+-1指2+（-1）=1
#4 python中前导0为八进制格式
#5 两值没有运算符即一个数，将直接输出

#%%1.2.1
seconds=42*60+42
print('1.2.1_秒数为')
print(seconds)

#%%1.2.2
distance=1/1.61*10
print('1.2.2_英里数为')
print(distance)

#%%1.2.3
PACE=(seconds//60)/distance + (seconds%60)/distance
print('1.2.3_平均配速为')
print(PACE)
#//指整除，%指取余数






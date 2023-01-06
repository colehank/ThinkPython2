#%%2.1
#1_不能将数字赋值给字母
#2 合法，x与y都被赋值给1
#3 合法，分号代表一个命令的结束，换行也可以代表一个任务的结束
#4 python中的运算要有运算符，xy如果没被定义是没有意义的。

#%%2.2.1
import math
r=5
V=3/4*math.pi*r**2
print('1_球的体积为：')
print(V)

#%%2.2.2
price=24.95*60*0.4 + 3+59*0.75
print('2_总价为')
print(price)

#%%2.2.3
import datetime
time_easy=2*(8+15/60)
time_tempo=3*(7+12/60)
time_total=time_tempo+time_easy
time_leaving='2022-10-18 06:52:00'#如果不加年份输出结果自动会加上1900-1-1
dateleaving=datetime.datetime.strptime(time_leaving, "%Y-%m-%d %H:%M:%S") #将str转换为time格式
time_arriving=dateleaving+datetime.timedelta(minutes=time_total)#基于time格式加分钟数获得抵达时间
print('3_到达时间为')
print(time_arriving)




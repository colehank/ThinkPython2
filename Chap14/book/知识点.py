'持久'
#指数据储存，本地文件是持久的，很多网页是不持久的

'读写'
#open
fout = open('output.txt', 'w')#若文件存在，便覆盖掉，不存在，便创建
#参数w是write的意思

line1 = "This here's the wattle,\n"
fout.write(line1)#这个函数会返回写入的字符的数量
line2 = "the emblem of our land.\n"
fout.write(line2)
fout.close()#关闭文件，若不，要等这个文件关了之后他才会关

'%格式运算符'
#write写入的方法只接受字符串，要转化，最简单str（）
#另一种：%（格式运算符）///当%用于int，是整除，用于str则是格式运算符

x = 4
'%d'% x#'42'
#这样可以在字符串内嵌入变量了
' the price is %d' %x#' the price is 4'
 
'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')#'In 3 years I have spotted 0.1 camels.'
#//格式化序列大于一个，后面就要用元组表达了,如上，
'%d用于int，%g用于float，%s用于字符串'

'os模块'
import os
cwd = os.getcwd()
cwd#返回当前工作的绝对路径

os.path.exists('output.txt')#检查对象是否存在
#///注：文件名也可以是相对路径
os.path.isdir('output.txt')#检查对象是否是一个目录
#///注：此处判断的是绝对路径
os.path.isfile('output.txt')
#///注：此处判断是否是文件
os.listdir(cwd)
#///类似 unix的ls，返回目录内文件

def walk(dirname):
#"把目录下所有文件名和文件内的目录的文件名打印出来"
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
os.path.join
#///接受一个目录和文件名，将他们拼接为完整的路径

walk('/Users/harrischeung/Documents/GitHub/freshman_of_python/think_python/Chap14')

'捕获异常'
try:
    fin = open('bad file')
except:#python先执行try，如果正常就会跳过except
    print('Something went wrong.')
    
######################################################################################

'数据库'
import dbm#创建和更新数据库文件的交互接口
db = dbm.open('captions','c')#前者是打开文件的名字，后者是'c'是一个模式，指不存在该数据库就建一个新的
#该函数返回一个数据库对象

db['cleese.png'] = 'photo of john cleese' #在数据库更新一个新的项
db['cleese.png']#读取项
db['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
db['cleese.png']#此时，新值会覆盖旧值

for key in db:
    print(key, db[key])#字典的一些方法不适用于数据库对象，可以用for循环迭代
    
db.close()#数据库用完了得用close关闭

######################################################################################

#dbm的局限在于值和键值必须是str或二进制，而pickle模块可以把几乎所有对象翻译为str储存，用时再翻译回来

'Pickle模块'#将非字符串数据转译为str，储存在数据库里
import pickle
t = [1, 2, 3]
t1 = pickle.dumps(t)#pickle.dumps把对象翻译为str
t2 = pickle.loads(t1)#pickle.lods把存储的str解释为原对象

t == t2#True
t is t2#False
#原对象和翻译输出的对象值一样，但是通常不是一个个对象，pickle解释过程相当于复制原对象


'shell'#命令行接口
#shell可以启动所有程序，在python要实现的话需要pipe对象

'pipe'#python到shell的通信途径，一个pipe代表一个运行的程序
import os
cmd = 'ls'
fp = os.popen(cmd)#实参要是一个shell命令的字符串，返回一个行为（ls -l:已打开的文件对象）
res = fp.read()#read指读取工作目录下所有，若readline则为只读取一行
res

stat = fp.close()
print(stat)#返回None说明正常结束，无错误

######################################################################################

'编写模块'
import wc
wc.linecount('知识点.py')#模块.函数（实参）
#模块内如果有要运行的代码，加上if __name__ = __'main'__,这也仅有在模块文件内才会运行次代码，在导入的文件则不会


s = '1 2\t 3\n 4'
print(s)

s = '1 2\t 3\n 4'
print(repr(s))#把空格和换行在输出的时候用字符串表示，眼睛看可能不太明显










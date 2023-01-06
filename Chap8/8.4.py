def any_lowercase1(s):
    for c in s:
        if c.islower():
            #如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
            #当有一个是小写的时候，由于return的存在，程序被退出
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            #‘c’肯定是小写形式，该结果永恒正确,即使形参都是大写
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        #对于每一个字母都可以得到正确判断，但是每一次的结果会被刷新，
        #只会保存最后一次的结果,打印所有结果即可观察
        print('3',c,flag)
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        #，通过or操作，会将结果为真的保留下来
        print('4',flag,c.islower())
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            print(c)#遇到结果为大写的时候，函数被停止，返回错误结果
            return False
    return True

print('result1',any_lowercase1('abcDEF'))
print('result2',any_lowercase2('abcDEF'))
print('result3',any_lowercase3('abcDEF'))
print('result4',any_lowercase4('abcDEF'))
print('result5',any_lowercase5('abcDEF'))

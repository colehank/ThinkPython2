#%%3.1
def right_justify(s):
    print(' '*(70-len(s)) + s)
print('3.1结果如下')
right_justify('monthy ')

#%%3.2.1
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
print('3.2.1结果如下')
do_twice(print_spam)

#%%3.2.2
def do_twice(f,a):
    f(a)
    f(a)
print('3.2.2由题将a传递给f并调用f两次')
#%%3.2.3
def print_twice(bruce):
    print(bruce)
    print(bruce)
print('3.2.3由题复制前文定义')
#%%3.2.4
print('3.2.4结果如下')
do_twice(print_twice,'spam') #()spam作为实参传递给了print_twice，print_twice的结果作为实参由do_twice处理

#%%3.2.5
def do_four(z,b):
    do_twice(z,b)
    do_twice(z,b)
print('3.2.5定义了函数do_four')
#%%3.3
def print_X():
    print('+ - - - - + - - - - +')

print('3.3 以下为grid')
print_X()
do_four(print,'|         |         |')
print_X()
do_four(print,'|         |         |')
print_X()


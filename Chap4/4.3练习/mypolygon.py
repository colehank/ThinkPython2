import turtle
bob = turtle . Turtle ()
print ( bob )
#fd-forward、lt-left、rt-right、bk（back），just painted a square
#Turtle仅有两种状态：pu-pen _up、pd-pen_down


for i in range(4):
    print('hello!')
    
for i in range(4):
    bob.fd (100)
    bob.lt (90)
turtle . mainloop () #mainloop 告诉窗口等待用户操作

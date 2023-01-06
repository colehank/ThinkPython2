import math

def my_sqrt(a):
    epsilon=0.00000001
    x=4
    while True: 
        y = (a + x/a) / 2 
        if abs(y-a)<epsilon:#此处epsilon为决定精读的一个值，入0.0000001
            break 
        a=y
    return a

def test_square_root(a):
    print('a'+' '*5+'mysqrt(a)'+' '*4+'math.sqrt'+' '*6+'diff')
    print('___'+' '*5+'_'*9+' '*4+'_'*9+' '*6+'_'*4)
    for a in range(1,a+1):
        mysqrt=my_sqrt(a)
        mathsqrt=math.sqrt(a)
        print('%.1lf  \t%lf  \t%lf  \t%lf' % (a,mysqrt, mathsqrt, abs(mysqrt-mathsqrt)))

test_square_root(10)



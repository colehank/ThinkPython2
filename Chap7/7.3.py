import math

def factorial(n):
    if n == 0:
        return 1
    else:
        rescurse = factorial(n-1)
        result = n*rescurse
        return result
    
#factoria(3)=3*factoria(2)
#factoria(2)=2*factoria(1)
    
def estimate_pi(n):
    x = 0
    a = 2*math.sqrt(2)/9801
    if n <0:
        print('请输入一个大于0的整数')
    elif n==0:
        pi=1/(a*1103)
        return pi
    else:
        for k in range(n):
            b = factorial(4*k)
            c=1103+26309*k
            d=factorial(k)**4
            e=396**(4*k)
            x=b*c/d/e+x
        s=a*x
        pi=1/s
        return pi
    
print(estimate_pi(1))

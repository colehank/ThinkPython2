def compare(x,y):
    if x>y:
        return 1
    if x==y:
        return 0
    if x<y:
        return-1
        
        
import math
      
def distance(x1,y1,x2,y2):
    d1=(x2-x1)
    d2=(y2-y1)
    return(math.sqrt(d1**2+d2**2))

distance(1,2,4,6)


def hypotenuse(a,b):
    return(math.sqrt(a**2+b**2))

hypotenuse(3,4)


#6.4 return的直接是布尔值
def is_between(x,y,z):
    return x<=y<=z

is_between(1, 2, 3)

#6.5 back to recursion

def factorial(n):
    if n==0:
        return 1
    else:
        recurse= factorial(n-1)
        result=recurse*n
        return result
#这个看了很久，细看。是factorial（n-1）在递归，下一个递归就是n-1（f（n-1-1））直到n=0返回1

def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    



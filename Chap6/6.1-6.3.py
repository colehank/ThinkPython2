#6.1
def b(z):
    prod = a(z,z)
    print(z,prod)
    return prod
def a(x,y):
    x=x+1
    return x*y
def c(x,y,z):
    total = x+y+z
    square = b(total)**2
    return square

x = 1
y = x+1
print(c(x,y+3,x+y))

#第一个：5+2x，第二个：第一个数*（第一个数+1），第三个：第二个数的平方

#6.2
def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
#这个函数的增长非常块，（4，3）就已经无法确定位数了

print(ack(3,4))

#6.3
import palindrome

def is_palindrome(word):
    if len(word)<2:
        return True
    if palindrome.first(word) == palindrome.last(word) and is_palindrome(palindrome.middle(word)):
        return True
    else:
        return False

        
while True:
    s=input('>')
    if s == 'quit':
        break
    print(is_palindrome(s))
    


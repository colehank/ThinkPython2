import turtle
bob = turtle.Turtle ()

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt (360/n)
#4.3.4
import math
def circle(t,r):
    c = 2*math.pi*r
    n = 300#随意举例的
    length = c/n
    polygon(t,length,n)

circle(bob, 100)

turtle . mainloop ()

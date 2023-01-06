import turtle
bob = turtle.Turtle ()

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt (360/n)
#4.3.4
import math
def arc(t,r,angle):
    c = 2*math.pi*r
    n = 200#随意举例的
    length = c/n
    for i in range(angle):
        t.fd(length)
        t.lt (360/n)

arc(bob,100,20)

turtle . mainloop ()

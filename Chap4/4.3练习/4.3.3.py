import turtle
bob = turtle.Turtle ()

#4.3.3

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt (360/n)
polygon(bob,300,10)

turtle . mainloop ()


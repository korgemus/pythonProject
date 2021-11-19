from turtle import *


def circ(x):
    circle(x)

color('green')
begin_fill()

a=list(map(int,input().split()))
max=a[0]
for w in a:
    if (w>max) & (w<=200):
        max=w
for i in a:
    if i>200:
        color('blue')
        circ(20)
    elif i==max:
        color('red')
        circ(i)
    else:
        color('green')
        circ(i)
exitonclick()
print(max)

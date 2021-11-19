from turtle import *


# def circ(x):
#     circle(x)
#
# color('green')
# begin_fill()
#
# a=list(map(int,input().split()))
# max=a[0]
# for w in a:
#     if (w>max) & (w<=200):
#         max=w
# for i in a:
#     if i>200:
#         color('blue')
#         circ(20)
#     elif i==max:
#         color('red')
#         circ(i)
#     else:
#         color('green')
#         circ(i)
# exitonclick()
# print(max)
def qudr(x):
    forward(x)
    left(90)
    forward(x)
    left(90)
    forward(x)
    left(90)
    forward(x)
    left(90)

color('green')
begin_fill()
penup()
setposition(-400,-380)
pendown()
m=int(input())
c=int(input())
for i in range(0,c):
    qudr(m)
    m=m/2
exitonclick()
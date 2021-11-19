

n=int(input())
if n<10 :
    n=n*1000
if n<100 :
    n=n*100
if n<1000 :
    n=n*10
a=n//1000
n=n%1000
b=n//100
n=n%100
c=n//10
n=n%10
d=n%10
if (a==d) and (b==c) :
    print("1")
else:
    print("2")


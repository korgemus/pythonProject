a=list(map(int,input().split()))
b=a[0]
c=a[1]
d=a[2]
if d==b & d==c:
    print("3")
elif (b==c) | (b==d) | (c==d):
    print("2")
else:
    print("0")


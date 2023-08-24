n=int(input())
a=[]
b=[]
while n:
    d=n%10
    n=n//10
    a.append(d)
for i in a:
    if i%2!=0:
        b.append(i**2)
c=b[::-1]
for i in c:
    print(i,end='')
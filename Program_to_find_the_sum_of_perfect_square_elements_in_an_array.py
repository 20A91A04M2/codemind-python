n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    k=int(i**(1/2))
    if k*k==i:
        c+=i
print(c)
        
m=int(input())
a=list(map(int,input().split()))
sum=0
flag=0
for i in range(m):
    if i%2==0:
        sum+=a[i]
    else:
        flag+=a[i]
print(sum-flag)        
        
        
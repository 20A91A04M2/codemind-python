l,r,k=map(int,input().split())
flag=0
for i in range(l,r+1):
    if i%k==0:
        flag=flag+1
print(flag)    
        
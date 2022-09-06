m=int(input())
sum=0
for i in range(1,m):
    if m%i==0:
        sum=sum+i
n=int(input())
flag=0
for j in range(1,n):
    if n%j==0:
        flag=flag+j
if sum==n and flag==m:
    print('Amicable')
else:
    print('Not Amicable')

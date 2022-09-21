n=int(input())
lst=list(map(int,input().split()))
k=sum(lst)/n
print('{:.2f}'.format(k))

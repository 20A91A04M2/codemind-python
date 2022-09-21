n=int(input())
lst=list(map(int,input().split()))
k=sum(lst)//n
if k in lst:
    print('True')
else:
    print('False')
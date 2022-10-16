n=int(input())
k=list(map(int,input().split()))
l=[]
for i in k:
    if i not in l:
        l.append(i)
for i in l:
    print(i,end=' ')
    
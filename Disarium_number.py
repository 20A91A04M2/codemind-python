n=int(input())
a=str(n)
c=0
for i in a:
    k=int(i)**(a.index(i)+1)
    c+=k
if c==n:
    print('True')
else:
    print('False')
    
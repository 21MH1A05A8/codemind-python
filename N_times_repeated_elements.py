n=int(input())
l=list(map(int,input().split()))
k=int(input())
r=[]
for i in l:
    if k==l.count(i):
        if i not in r:
            r.append(i)
if len(r)==0:
    print(-1)
else:
    print(*r)

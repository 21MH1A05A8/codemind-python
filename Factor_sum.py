def factor(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
l=list(map(int,input().split(",")))
r=[]
for i in l:
    s=factor(i)
    if s in l:
        r.append(i)
if len(r)==0:
    print(-1)
else:
    print(*sorted(r))
        
    
n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
r=[]
for i in  k:
    if i>=a and i<=b:
        r.append(i)
if len(r)==0:
    print(-1)
else:
    print(min(r))
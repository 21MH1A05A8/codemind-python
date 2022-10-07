n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if i==l.count(i):
        r.append(i)
if len(r)==0:
    print("-1")
mi=min(r)
mx=max(r)
print(mi,mx)
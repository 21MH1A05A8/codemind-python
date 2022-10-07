n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
z=set(l).intersection(k)
r=[]
for i in l:
    if i not in z:
        r.append(i)
for i in k:
    if i not in z:
        r.append(i)
print(*r)
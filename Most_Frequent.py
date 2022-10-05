n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    s=l.count(i)
    k.append(s)
ma=max(k)
l1=[]
for i in l:
    if l.count(i)==ma:
        l1.append(i)
print(min(l1))
        
n=int(input())
l=list(map(int,input().split()))
r=[]
c=0
for i in l:
    if i==l.count(i):
        if i not in r:
            r.append(i)
            c+=1
print(c)
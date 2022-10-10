n=int(input())
p=list(map(int,input().split()))
v=[]
c=[]
for i in range(n):
    if p[i]%2==0:
        c.append(p[i])
    else:
        v.append(p[i])
i,j=0,0
while i<len(v) or j<len(c):
    if i<len(v):
        print(v[i],end=" ")
        i+=1
    if j<len(c):
        print(c[j],end=" ")
        j+=1
if n%2!=0:
    print("0")
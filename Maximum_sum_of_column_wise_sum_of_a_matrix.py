n,m=map(int,input().split())
b=[]
for i in range(n):
    p=list(map(int,input().split()))
    b.append(p)
v=[]
for j in range(m):
    s=0
    for i in range(n):
        s+=b[i][j]
    v.append(s)
    s=0
print(max(v))
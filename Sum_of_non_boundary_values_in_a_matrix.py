n,m=map(int,input().split())
b=[]
x=0
for i in range(n):
    a=list(map(int,input().split()))
    b.append(a)
s=0
for i in range(n):
    for j in range(m):
        if i==0 or i==n-1 or j==0 or j==m-1:
            pass
        else:
            s+=b[i][j]
print(s)
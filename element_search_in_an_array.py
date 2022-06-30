n=int(input())
k=list(map(int,input().split()))
m=int(input())
f=0
for i in k:
    if i==m:
        f+=1
if f==0:
    print(False)
else:
    print(True)

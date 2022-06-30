n=int(input())
k=list(map(int,input().split()))
s,f=0,0
for i in k:
    s+=i
avg=s//n
for i in k:
    if avg==i:
        f+=1
if f==0:
    print(False)
else:
    print(True)

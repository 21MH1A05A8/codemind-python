n=int(input())
k=list(map(int,input().split()))
s,c=0,0
for i in k:
    s+=i
avg=s//n
for i in k:
    if i<=avg:
        c+=1
print(c)

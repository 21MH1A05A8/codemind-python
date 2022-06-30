n=int(input())
k=list(map(int,input().split()))
m=int(input())
s=0
for i in k:
    if i>m:
        break
    else:
        s+=i
print(s)
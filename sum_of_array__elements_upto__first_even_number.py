n=int(input())
k=list(map(int,input().split()))
s=0
for i in k:
    if i%2==0:
        break
    else:
        s+=i
print(s)
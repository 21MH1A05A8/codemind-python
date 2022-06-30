n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in k:
    if i>=a and i<=b:
        s+=i
print(s)
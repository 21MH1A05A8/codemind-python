def prime(n):
    if n==1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
k=list(map(int,input().split()))
m=int(input())
c=0
for i in k:
    if prime(i) and i<=m:
        c+=1
print(c)

def prime(n):
    if n==1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if prime(i):
        c+=1
print(c)
            
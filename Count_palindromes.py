def palin(n):
    t=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==t:
        return True
    else:
        return False
n=int(input())
k=list(map(int,input().split()))
c=0
for i in k:
    if palin(i):
        c+=1
print(c)
    
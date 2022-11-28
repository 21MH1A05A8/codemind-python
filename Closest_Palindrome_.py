def palin(n):
    t=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if t==rev:
        return True
    else:
        return False
n=int(input())
mi,mx=0,0
for i in range(11,n):
    if palin(i):
        mi=n-i
        s=i
for i in range(n+1,100000):
    if palin(i):
        mx=i-n
        s1=i
        break
if mi<mx:
    print(s)
elif mx<mi:
    print(s1)
else:
    print(s,s1)
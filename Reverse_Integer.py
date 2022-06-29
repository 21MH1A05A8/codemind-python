n=int(input())
rev,f=0,0
if n<0:
    n*=-1
    f+=1
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
if f==0:
    print(rev)
else:
    print(-1*rev)
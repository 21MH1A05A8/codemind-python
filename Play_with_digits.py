def add(n):
    s=0
    while n:
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input())
k=list(map(int,input().split()))
e=0
for i in k:
    e+=add(i)
print(e)
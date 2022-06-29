def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
s=n+m
for i in range(1,10000):
    if prime(i+s):
        print(i)
        break
        
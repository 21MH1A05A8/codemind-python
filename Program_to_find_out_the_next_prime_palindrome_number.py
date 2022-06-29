def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
def palin(n):
    rev=0
    t=n
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==t:
        return True
    else:
        return False
n=int(input())
for i in range(n+1,100000):
    if prime(i) and palin(i):
        print(i)
        break


        
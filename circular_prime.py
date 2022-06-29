def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
rev=0
if prime(n):
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if prime(rev):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')
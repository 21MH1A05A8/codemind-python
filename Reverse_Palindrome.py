def revr(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
def palin(n):
    if revr(n)==n:
        return n
def add(n):
    while n:
        s=revr(n)
        n+=s
        if palin(n):
            print(n)
            break
n=int(input())
add(n)

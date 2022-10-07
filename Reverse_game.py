def revr(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(revr(i),end=" ")
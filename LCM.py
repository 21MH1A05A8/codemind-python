n,m=map(int,input().split())
for i in range(n,10000):
    if i%n==0 and i%m==0:
        print(i)
        break
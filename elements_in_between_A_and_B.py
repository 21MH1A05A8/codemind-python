n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in k:
    if i>=a and i<=b:
        print(i,end=' ')
        s+=1
if s==0:
    print('-1')
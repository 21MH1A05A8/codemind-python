n=int(input())
l=list(map(int,input().split()))
s=0
if n%2!=0:
    s+=1
for i in l:
    print(i,end=" ")
if s==1:
    print(0)
n=int(input())
k=list(map(int,input().split()))
o=0
for i in k:
    if i%2==0:
        o+=i
print(o)
   
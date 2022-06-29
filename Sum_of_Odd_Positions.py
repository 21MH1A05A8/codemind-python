n=int(input())
k=list(map(int,input().split()))
o=0
for i in range(len(k)):
    if i%2!=0:
        o+=k[i]
print(o)
   
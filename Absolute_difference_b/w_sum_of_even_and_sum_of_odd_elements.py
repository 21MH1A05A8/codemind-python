n=int(input())
k=list(map(int,input().split()))
e,o=0,0
for i in k:
    if i%2==0:
        e+=i
    else:
        o+=i
print(abs(e-o))
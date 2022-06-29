n=int(input())
k=list(map(int,input().split()))
e,o=0,0
for i in range(len(k)):
    if i%2==0:
        e+=k[i]
    else:
        o+=k[i]
print(abs(e-o))
n=int(input())
k=list(map(int,input().split()))
f=0
for i in range(len(k)):
    if i+1==n:
        break
    else:
        if k[i]<k[i+1]:
            f+=1
if f==0:
    print('yes')
else:
    print('no')
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if(l[i]%2==0 and i%2!=0):
            c+=1
            break
if c==0:
    print(True)
else:
    print(False)
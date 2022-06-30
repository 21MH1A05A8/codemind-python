n=int(input())
k=list(map(int,input().split()))
s=0
for i in range(len(k)):
    if k[i]%2!=0:
        s=i
print(s)
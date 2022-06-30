n=int(input())
k=list(map(int,input().split()))
c,l=0,0
for i in k:
    c+=i
s=c//n
for i in k:
    if i>=s:
        l+=1
print(l)
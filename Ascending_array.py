n=int(input())
l=list(map(int,input().split()))
c=0
min=0
for i in l:
    if min<i:
        min=i
        c+=1
if c==len(l):
    print("yes")
else:
    print("no")

n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
r=[]
for i in l:
   if  i>=a and i<=b:
       continue
   else:
       r.append(i)
if len(r)==0:
    print(-1)
else:
    print(max(r))

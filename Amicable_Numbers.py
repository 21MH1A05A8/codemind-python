n=int(input())
m=int(input())
s,s1=0,0
for i in range(1,n):
    if n%i==0:
        s+=i
for i in range(1,m):
    if m%i==0:
        s1+=i
if s1==n and s==m:
    print("Amicable")
else:
    print("Not Amicable")
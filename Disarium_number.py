n=int(input())
k=str(n)
l=len(k)
num=n
s=0
while num:
    r=num%10
    s=s+int(pow(r,l))
    num=num//10
    l=l-1
if s==n:
    print(True)
else:
    print(False)
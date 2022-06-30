n=input()
n=n.lower()
m=input()
m=m.lower()
k=list(n)
s=set(m)
f=0
for i in k:
    if i not in s:
        f+=1
if f==0:
    print(True)
else:
    print(False)
n=input()
n=n.lower()
n=list(n)
c=0
r=[]
for i in n:
    if i!=" ":
        if n.count(i)==1:
            r.append(i)
s=sorted(r)
print("".join(s))
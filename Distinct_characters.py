n=input()
n=n.lower()
n=list(n)
r=[]
for i in n:
    if i!=" ":
        if n.count(i)==1:
            r.append(i)
r=sorted(r)
print("".join(r))
n=input()
n=n.lower()
r=[]
for i in n:
    if i!=" ":
        if i not in r:
            r.append(i)
print(len(r))

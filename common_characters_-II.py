s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
r=[]
for i in s1:
    for j in s2:
        if i==j and i!=" ":
            if i not in r:
                r.append(i)
print(len(r))
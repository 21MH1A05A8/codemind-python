s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=set(s1)
s2=set(s2)
s=s1.intersection(s2)
k=s1.union(s2)
k=list(k)
c=0
for i in k:
    if i!=" ":
        if i not in s:
            c+=1
print(c)
    

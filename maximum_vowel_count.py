n=input()
n=n.lower()
k=n.split()
m=0
for i in k:
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    if c>m:
        m=c
print(m)
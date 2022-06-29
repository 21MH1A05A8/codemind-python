n=input()
k=n.split()
e=[]
for i in k:
    s=i[::-1]
    e.insert(0,s)
print(*e)
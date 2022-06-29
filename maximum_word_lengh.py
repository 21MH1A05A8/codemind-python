n=input()
k=n.split()
max=0
for i in k:
    s=str(i)
    l=len(s)
    if l>max:
        max=l
print(max)
n=input()
k=n.split()
min=9999
for i in k:
    s=str(i)
    l=len(s)
    if l<min:
        min=l
print(min)
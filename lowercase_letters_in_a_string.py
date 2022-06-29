n=input()
k=list(n)
c=0
for i in k:
    if i.islower():
        c+=1
print(c)
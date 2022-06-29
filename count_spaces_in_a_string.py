n=input()
k=list(n)
c=0
for i in k:
    if i in ' ':
        c+=1
print(c)
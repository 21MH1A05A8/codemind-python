n=input()
k=list(n)
c=0
for i in k:
    if i in ' ':
        continue
    else:
        c+=1
print(c)
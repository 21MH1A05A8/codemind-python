n=input()
k=list(n)
c=0
for i in k:
    if i.islower():
        continue
    if i.isupper():
        continue
    if i.isdigit():
        continue
    if i in ' ':
        continue
    else:
        c+=1
print(c)
    
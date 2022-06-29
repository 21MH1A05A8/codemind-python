n=input()
k=list(n)
v='aeiouAEIOU'
c=0
for i in k:
    if i in v:
        c+=1
print(c)
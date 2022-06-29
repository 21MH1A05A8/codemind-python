def palin(n):
    s=n[::-1]
    if s==n:
        return True
    else:
        return False
n=input()
n=n.lower()
k=n.split()
c=0
for i in k:
    if palin(i):
        c+=1
print(c)

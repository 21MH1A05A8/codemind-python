n=input()
k=n.split()
for i in range(len(k)):
    if i==0:
        m=min(k[i])
    if i==len(k)-1:
        k=max(k[i])
print(m,k,end=' ')
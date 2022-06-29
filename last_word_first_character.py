n=input()
k=n.split()
for i in range(len(k)):
    if i==len(k)-1:
        for j in k[i]:
            print(j)
            break
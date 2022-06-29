n=input()
k=n.split()
for i in range(len(k)):
    if i%2==0:
        s=k[i][::-1]
        print(s,end=' ')
    else:
        print(k[i],end=' ')
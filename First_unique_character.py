n=input()
k=list(n)
f=0
for i in k:
    if k.count(i)==1:
        print(i)
        f+=1
        break
if f==0:
    print('-1')

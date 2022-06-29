n=input()
k=list(n)
c=0
e=[]
for i in k:
    if i in 'AEIOUaeiou':
        if i not in e:
            e.append(i)
            c+=1
if c==0:
    print('-1')
else:
    print(*e)
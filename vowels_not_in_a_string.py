n=input()
k=list(n)
e=[]
r=[]
s=0
for i in k:
    if i in 'aeiou':
        if i not in e:
            e.append(i)
if len(e)==5:
    print(0)
    s+=1
else:
    for i in 'aeiou':
        if i not in e:
            r.append(i)
if s==0:
    print(*sorted(r))
            
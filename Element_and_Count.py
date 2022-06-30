n=int(input())
k=list(map(int,input().split()))
e=[]
for i in k:
    if i not in e:
        e.append(i)
for i in e:
    s=k.count(i)
    print(i,s,end=' ')
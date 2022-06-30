n=int(input())
k=list(map(int,input().split()))
e=[]
for i in k:
    if i not in e:
        e.append(i)
print(*e)
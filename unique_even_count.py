n=int(input())
k=list(map(int,input().split()))
e=[]
s=0
for i in k:
    if i not in e:
        e.append(i)
for i in e:
    if i%2==0:
        s+=1
print(s)
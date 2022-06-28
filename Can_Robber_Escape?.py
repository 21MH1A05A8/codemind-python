n=int(input())
k=list(map(int,input().split()))
add=0
for i in k:
    if i%2!=0:
        add+=1
if add<=2:
    print('YES')
else:
    print('NO')
        
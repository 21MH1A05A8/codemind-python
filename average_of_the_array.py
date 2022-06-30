n=int(input())
k=list(map(int,input().split()))
s=0
for i in k:
    s+=i
avg=s/n
print('%.2f'%avg)
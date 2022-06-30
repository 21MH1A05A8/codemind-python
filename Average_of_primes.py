def prime(n):
    if n==1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
k=list(map(int,input().split()))
s,c=0,0
for i in k:
    if prime(i):
        s+=i
        c+=1
avg=s/c
print('%.2f'%avg)
n=int(input())
s=n*n
e=0
while s:
    r=s%10
    e+=r
    s=s//10
if e==n:
    print('Neon Number')
else:
    print('Not Neon Number')
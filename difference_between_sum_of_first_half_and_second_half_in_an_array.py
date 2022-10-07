n=int(input())
l=list(map(int,input().split()))
s,s1=0,0
for i in range(n//2):
    s+=l[i]
for i in range(n//2,n):
    s1+=l[i]
print(abs(s-s1))
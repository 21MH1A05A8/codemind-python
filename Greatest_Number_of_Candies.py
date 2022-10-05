n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=max(l)
for i in l:
    if i==s or i+k>=s:
        print("True",end=" ")
    else:
        print("False",end=" ")

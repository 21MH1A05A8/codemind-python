n=int(input())
k=list(map(int,input().split()))
s=0
for i in k:
    s+=i
l=s/n
print("{:.2f}".format(l))
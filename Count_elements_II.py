n,m=map(int,input().split())
k=list(map(int,input().split()))
l=list(map(int,input().split()))
k=set(k)
l=set(l)
s=k.intersection(l)
u=k.union(l)
print(len(u)-len(s))
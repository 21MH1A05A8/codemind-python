n=input()
k=list(n)
c=0
for i in k:
    if k.count(i)==1:
        c+=1
if len(k)==c:
    print(True)
else:
    print(False)
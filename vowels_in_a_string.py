n=input()
m=input()
k=list(n)
for i in range(len(k)):
    if k[i] in m:
        print(True)
        print(i)
        break
else:
    print(False)

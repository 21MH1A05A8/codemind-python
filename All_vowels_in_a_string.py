n=input()
v="aeiou"
r=[]
for i in n:
    if i in v:
        if i not in r:
            r.append(i)
if len(r)==5:
    print(True)
else:
    print(False)
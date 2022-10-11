n=input()
v='aeiou'
s='AEIOU'
c,p=0,0
v1=[]
v2=[]
for i in n:
    if i!=" ":
        if i in v:
            if i not in v1:
                v1.append(i)
        elif i in s:
            if i not in v2:
                v2.append(i)
if len(v1)==5 or len(v2)==5:
    print(True)
else:
    print(False)
        
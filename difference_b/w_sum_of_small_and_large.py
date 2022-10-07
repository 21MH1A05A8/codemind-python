n=input()
n=n.split()
s,s1=0,0
for i in n:
    s+=ord(min(i))
    s1+=ord(max(i))
print(abs(s-s1))
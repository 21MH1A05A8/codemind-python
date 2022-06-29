def num(n):
    a=str(n)
    if '6' in a:
        k=list(a)
        e=k.index('6')
        k[e]='9'
        g="".join(k)
        return int(g)
    else:
         return n
n=int(input())
print(num(n))
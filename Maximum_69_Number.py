def num(n):
    a=str(n)
    if '6' in a:
        l=list(a)
        e=l.index('6')
        l[e]='9'
        g="".join(l)
        return int(g)
    else:
        return n
n=int(input())
print(num(n))
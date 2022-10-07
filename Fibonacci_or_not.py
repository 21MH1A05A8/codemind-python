def fib(n):
    a,b=0,1
    f=0
    for i in range(2,n):
        c=a+b
        a,b=b,c
        if c==n:
            f+=1
    if f==1:
        print("True")
    else:
        print(False)
n=int(input())
fib(n)
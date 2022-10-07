def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
c=0
for i in range(2,n):
    for j in range(2,n):
        if prime(i) and prime(j):
            if i<j:
                if i*j==n:
                    print(i,j)
                    c+=1
                    break
if c==0:
    print(-1)
    
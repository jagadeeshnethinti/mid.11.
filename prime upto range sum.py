n=int(input())
t=0
for i in range(2,n+1):
    j=1
    c=0
    while(j<=i):
        if i%j==0:
            c=c+1
        j=j+1
    if c<=2:
        t=t+i
print(t)
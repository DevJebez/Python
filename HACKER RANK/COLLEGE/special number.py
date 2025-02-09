m=int(input())
n=int(input())
sum=a=b=g=0
for i in range(m,n):
    g=i
    a=i%10
    b=a
    sum+=a
    i=i//10
    b*=i
    sum+=i
    result=sum+b
    sum=a=b=0
    if g==result:
        print(g)
    g=0
    

    
    

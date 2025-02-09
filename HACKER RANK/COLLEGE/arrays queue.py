n, m = map(int, input().split())
k = [int(k) for k in input().split(" ")]
b=0
x=1
if len(k)>n:
    k=k[0:n]
print(k)
for i in range(n):
    if k[i]< m and i!=n-1:
        if k[i+1]+k[i]<=m: 
            b+=1
    elif k[i]<m and i==n-1:
        b+=1
    else:
        while x!=0:
            x=k[i]-m
            b+=1
print(b)

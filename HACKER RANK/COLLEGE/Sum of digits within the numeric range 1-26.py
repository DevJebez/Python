a=int(input())
l=len(str(a))
sum_a=0
v=0
op="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if a>=0 and a<=1000000000:
    for i in range(l):
        v=a%10
        sum_a=v+sum_a
        a=a//10
    if sum_a<=len(op):
        print(op[sum_a-1])
    if sum_a>26:
        g=0
        sum_a1=0
        for i in range(len(str(sum_a))):
            g=sum_a%10
            sum_a1=g+sum_a1
            sum_a=sum_a//10
        print(op[sum_a1-1])
else:
    print(-1)

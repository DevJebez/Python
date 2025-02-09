x=int(input())
g=x
y=str(abs(x))
if x<0:
    x=abs(x)
l=len(y)
s=0
d=l-1
a=10**d
for i in range(l):
    s=s+((x%10)*a)
    x//=10
    a//=10
print(s)
if g<0:
    s=-s
print(s)
print(g-s)

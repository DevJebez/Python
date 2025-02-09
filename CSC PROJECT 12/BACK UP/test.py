import csv
e=open('login.csv','r')
r=csv.reader(e)
table=[]
for i in r:
    print(i)    
    if len(i)>2:
        table.append(i)
l,x=[],[]
f=len(table[0])
for i in range(3): # for i in range(3)
    for r in table:
        print(r)
        y=str(r[i])
        g=len(y)
        x.append(g)
    l.append(max(x))
    x.clear()
print('l',l)
print(sum(l))
for g in l:
    pass

yr=int(input())
m=int(input())
a=31
b=30
c=29
if (yr>=1900 and yr<=9999) and (m>=1 and m<=12):
    if yr%4==0 and m==2:
        print(c,"Days")
    elif m in [1,3,7,8,10,12,5]:
        print(a,"Days")
    elif m in [4,6,9,11]:
        print(b,"Days")
    else:
        print(c-1,"Days")
else:
    print(0)
        

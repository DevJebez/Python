age=int(input())
yop=int(input())
fi=int(input())
na=int(input())
ma=float(input())
att=float(input())
maip=(ma*100)//100
attip=int(att)

if (age>=18 and age<21) and na<=2 and fi<=200000 and maip>=60 and attip>=80:
    print("Eligible")
elif na>2 and maip>=80 and attip>=90 and fi>200000 and fi<250000 :
    print("Partially Eligible")
else:
    print("Not Eligible")
    

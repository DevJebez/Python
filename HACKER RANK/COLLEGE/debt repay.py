p=float(input("Enter principal amount :"))
r=float(input("Enter rate of interest :"))
n=float(input("Ente no.of years :"))

i=p*r*n/100
amt=p+i
dis=(i*2.0)/100
final=amt-dis

print('%.2f' %i)
print('%.2f' %amt)
print('%.2f' %dis)
print('%.2f' %final)


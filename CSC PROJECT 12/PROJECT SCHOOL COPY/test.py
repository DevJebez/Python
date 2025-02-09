import csv
def userview(fg):
    e=open(fg,'r')
    r=csv.reader(e)
    table=[]
    for i in r:
        if len(i)>2:
            table.append(i)
    def show(table):
        l = [(max([len(str(row[i])) for row in table]) + 0) for i in range(len(table[0]))]
        r = "".join(["{:" + str(lc) + "}|" for lc in l])
        k=-1
        print(l)
        for row in table:
            k+=1
            a=str(k)
            if len(a)==1:
                a='0'+a
                if len(table[0])>5:
                    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                elif len(table[0])== 3:
                    print('--------------------------------')
            print(a+'|',r.format(*row))
    show(table)
    if len(table[0])>5:
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    elif len(table[0])==3:
        print('--------------------------------')    
    print()
    

def admin_choice():
    while True:
        print('\t\t\t\t|-------------------------------------------------------------|')
        print('\t\t\t\t|                           MAIN MENU                         |')
        print('\t\t\t\t|-------------------------------------------------------------|')
        print("\t\t\t\t|                 1.USER LOGIN DETAILS                        |")
        print("\t\t\t\t|                 2.CUSTOMER DETAILS                          |")
        print("\t\t\t\t|                 3.CUSTOMERS WHO'VE CANCELLED THEIR BOOKING  |")
        print("\t\t\t\t|                 4.LOG OUT                                   |")
        print('\t\t\t\t|-------------------------------------------------------------|')
        y=input('Enter your choice:')
        if y=='1':
            userview('login.csv')            
        if y=='2':
            userview('car_booking.csv')
            '''with open('car_booking.csv') as B:                
                red=csv.DictReader(B)
                cdd=[]
                for i in red:
                    print(json.dumps(dict(i),indent=4))
                    print()
            continue'''
        if y=='3':
            userview('cancelled_booking.csv')
        if y=='4':
            print('LOGGED OUT SUCCESSFULLY')
            break            
        else:
            print('Enter a valid choice\n')
            continue

admin_choice()

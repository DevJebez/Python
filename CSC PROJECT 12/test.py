import csv
with open('car_booking.csv ','a+') as G:
    r=csv.reader(G)
    w=csv.writer(G)
    h=[]
    for i in r:
        h.append(i)
    print(h)
        

import csv,random,sys,datetime,json
from datetime import date
f1=open('login.csv','a+',newline="")
f2=open('admin.csv','a+',newline="")
f3=open('car_booking.csv','a+',newline="")
f4=open('cancelled_booking.csv','a+',newline="")


def cars():
    def incars():
        print('\t\t\tBRAND')
        print('[1] Audi          [5] Honda      [9] Mercedes Benz [13] Rollsroyce')
        print('[2] BMW           [6] Hyundai    [10] Nissan       [14] Toyata')
        print('[3] Bugatti       [7] Lamborgini [11] Pagani       [15] Volkswagen')
        print('[4] Devel sixteen [8] Koenigsegg [12] Porsche      [16] Aston martin')
        global bb
        global c
        global p
        global cc
        a = int(input('Select the required brand:'))
        if a == 1:
            bb='Audi'
            print('[1]AUDI Q5')
            print('[2]AUDI Q7')
            print('[3]AUDI Q8')
            print('[4]AUDI A4')
            print('[5]AUDI A6')
            print('[6]AUDI Q2')
            print('[7]AUDI RS7')
            print('[8]AUDI A8L')
            print('[9]AUDI e-tron')
            print('[10]Audi e-tron GT')
            print('[11]AUDI RS etron GT')
            print('[12]AUDI RS Q8')
            print('[13]AUDI RS5')
            print('[14]AUDI RS5 SPORTSBACK')
            print('[15]AUDI A3')
            print('[16]AUDI Q3')
            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='AUDI Q5'                
                print('\tCC-1984')
                print('\tBHP-245.59@5000rpm')
                print('\tTorque-320Nm@1600-4500rpm')
                print('\tTRANSMISSION- Automatic')
                print('\tTOP SPEED -220kmph')
                print('\tMileage-13.45')
                print('\tTank capacity-85L')
                print('\tSeats-5')
                print('\tPrice-59-65.5 Lakhs')               
                p=6200000
            if model_C == 2:
                c='AUDI Q7'
                print('\tCC- 2995')
                print('\tBHP-335.25bhp@5000-6400rpm')
                print('\tTorque-370Nm@1600-4500rpm')
                print('\tTRANSMISSION- Automatic')
                print('\tTOP SPEED -240Kmph')
                print('\tMileage-11.2')
                print('\tTank capacity-75L')
                print('\tSeats-4')
                print('\tPrice-82.48 lakhs -89.89 lakhs')
                p=8500000
           
            if model_C == 3:
                c='AUDI Q8'
                print('CC-2995')
                print('BHP-335.25bhp@5000-6400rpm')
                print('Torque-320nm@1450–4200')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -220kmph')
                print('Mileage-9.8')
                print('Tank capacity-80L')
                print('Seats-5')    
                print('Price-55Lakhs')
                p=5500000

            if model_C == 4:
                c='AUDI A4'
                print('CC-1998')
                print('BHP-187.74bhp@4200-6000')
                print('Torque-320nm@1450–4200')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-17.42Kmpl')
                print('Tank capacity-54Litres')
                print('Seats-5')
                print('Price-49.97 Lakh')
                p=4997000

            if model_C == 5:
                c='AUDI A6'
                print('CC-1984')
                print('BHP-241.3bhp@5000-6500rpm')
                print('Torque-370Nm@1600-4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-14.11 Kmpl')
                print('Tank capacity-73Litres')
                print('Seats-5')
                print('Price-65.99Lakh')
                p=6599000

            if model_C == 6:
                c='AUDI Q2'
                print('CC-1984')
                print('BHP-187.74bhp@4200-6000rpm')
                print('Torque-320nm@1500–4180rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-6.5Kmpl')
                print('Tank capacity-55Litres')
                print('Seats-5')
                print('Price-34.99-48.89L')
                p=4889000

            if model_C == 7:
                c='AUDI RS7'
                print('CC-3996')
                print('BHP-591bhp@6000-6250rpm')
                print('Torque-800nm@2050-4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -220kmph')
                print('Mileage-8.9Kmpl')
                print('Tank capacity-73Litres')
                print('Seats-4')
                print('Price-2.24 Cr')
                p=22400000

            if model_C == 8:
                c='AUDI A8L'
                print('CC-2995')
                print('BHP-335.25bhp@5000-6400rpm')
                print('Torque-500nm@1370-4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-11kmpl')
                print('Tank capacity-73Litres')
                print('Seats-4')
                print('Price-1.57Cr')
                p=157000
                
            if model_C == 9:
                c='AUDI e-tron'
                print('CC-2995')
                print('BHP-300')
                print('Torque-630N.m')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Range-264-379km')
                print('Seats-5')
                print('Price-1.19Cr')
                p=11900000

            if model_C == 10:
                c='Audi e-tron GT'
                print('CC-2995')
                print('BHP-475 kW')
                print('Torque-830Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -220kmph')
                print('Range-388-500km')
                print('Seats-5')
                print('Price-1.66cr')
                p=16600000
            if model_C == 11:
                c='AUDI RS etron GT'
                print('CC-2995')
                print('BHP-636.98bhp')
                print('Torque-830Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -190kmph')
                print('Range-401-481km')
                print('charging time-5:15hrs(5-80#)')
                print('Seats-4')
                print('Price-1.89 Cr')
                p=18900000

            if model_C == 12:
                c='AUDI RS Q8'
                print('CC-3998')
                print('BHP-591.39bhp@6000rpm')
                print('Torque-800nm@2200-4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -200kmph')
                print('Mileage-8.26kmpl')
                print('Tank capacity-85Litres')
                print('Seats-5')
                print('Price-2.17cr')
                p=21700000

            if model_C == 13:
                c='AUDI RS5'
                print('CC-2984')
                print('BHP-443.87bhp@5700-6700rpm')
                print('Torque-600nm@1900-5000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-8.8kmpl')
                print('Tank capacity-58Litres')
                print('Seats-4')
                print('Price-1.09cr')
                p=10900000

            if model_C == 14:
                c='AUDI RS5 SPORTSBACK'
                print('CC-2894')
                print('BHP-443.87@5700-6700rpm')
                print('Torque-600nm@1900-5000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -230kmph')
                print('Mileage-8.8kmpl')
                print('Tank capacity-58Litres')
                print('Seats-4')
                print('Price-1.09cr')
                p=10900000

            if model_C == 15:
                c='AUDI A3'
                print('CC-1998')
                print('BHP-148 bhp @ 5000 rpm')
                print('Torque-250 Nm @ 1500 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -220kmph')
                print('Mileage-8.8kmpl')
                print('Tank capacity-58Litres')
                print('Seats-5')
                print('Price-35Lakhs')
                p=3500000

            if model_C == 16:
                c='AUDI Q3'
                print('CC-1984')
                print('BHP-148hp@3500-4000rpm')
                print('Torque-340Nm@1750-2750rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -190kmph')
                print('Mileage-12kmpl')
                print('Tank capacity-64Litres')
                print('Seats-5')
                print('Price-45Lakhs')
                p=4500000
            elif model_C < 1 or model_C > 16:
                print('Select the appropriate model ')
                cars()
        if a == 2:
            bb='BMW'
            print('[1]BMW X3')
            print('[2]BMW X6')
            print('[3]BMW 3 SERIES')
            print('[4]BMW 5 SERIES')
            print('[5]BMW X7')
            print('[6]BMW 2 SERIES')
            print('[7]BMW M4 COMPETITION')
            print('[8]BMW M5')
            print('[9]BMW X4')
            print('[10]BMW 7 SERIES')
            print('[11]BMW M2')
            print('[12]BMW X5 M')
            print('[13]BMW X1')
            print('[14]BMW iX')
            print('[15]BMW i4')
            print('[16]BMW 6 SERIES')
            print('[17]BMW Z4')
            print('[18]BMW 8 SERIES')
            print('[19]BMW X3 M')
            print('[20]BMW iX1')
            print('[21]BMW X1')
            print('[22]BMW i7')
            print('[23]BMW i8')
            print('[24]BMW M8')
            print('[25]BMW M5')
            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='BMW X3'
                print('CC-1998')
                print('BHP-248.08bhp@5200rpm')
                print('Torque-350nm@1450-4800rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-13.17kmpl')
                print('Tank capacity-63Litres')
                print('Seats-5')
                print('Price-61.90-67.90Lakhs')
                p=6790000

            if model_C == 2:
                c='BMW X6'
                print('CC-1998')
                print('BHP-335.25bhp@5500-6500rpm')
                print('Torque-450Nm@1500-5200rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-10.35kmpl')
                print('Tank capacity-83Litres')
                print('Seats-5')
                print('Price-1.04 Cr')
                p=10400000

            if model_C == 3:
                c='BMW 3 SERIES'
                print('CC-2998')
                print('BHP-382.19bhp@5800rpm')
                print('Torque-500Nm@1850-5000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-10.3kmpl')
                print('Tank capacity-59Litres')
                print('Seats-5')
                print('Price-46.90 - 68.90 Lakh')
                p=6890000

            if model_C == 4:
                c='BMW 5 SERIES'
                print('CC-2998')
                print('BHP-261.49bhp@4000rpm')
                print('Torque-620nm@2000–2500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-17.37kmpl')
                print('Tank capacity-63Litres')
                print('Seats-5')
                print('Price-46.90-69.90Lakhs')
                p=6990000

            if model_C == 5:
                c='BMW X7'
                print('CC-2993')
                print('BHP-394.26bhp@4400rpm')
                print('Torque-760nm@2000-3000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-12kmpl')
                print('Tank capacity-80Litres')
                print('Seats-5')
                print('Price-1.18 - 1.78 Cr')
                p=17800000

            if model_C == 6:
                c='BMW 2 SERIES'
                print('CC-2998')
                print('BHP-187.74bhp@4000rpm')
                print('Torque-400nm@1750-2500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-13.38kmpl')
                print('Tank capacity-50Litres')
                print('Seats-7')
                print('Price-41.50 - 44.50 Lakh')
                p=4450000

            if model_C == 7:
                c='BMW M4 COMPETITION'
                print('CC-1998')
                print('BHP-502.88bhp@6250rpm')
                print('Torque-650Nm@2750-5500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -230kmph')
                print('Mileage-18.64Kmpl')
                print('Tank capacity-50litres')
                print('Seats-5')
                print('Price-s.1.44 Cr')
                p=14400000

            if model_C == 8:
                c='BMW M5'
                print('CC-2993')
                print('BHP-616.87bhp@6000rpm')
                print('Torque-750nm@1800-5860rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -280kmph')
                print('Mileage-9.12kmpl')
                print('Tank capacity-40Litres')
                print('Seats-5')
                print('Price-1.44Crore')
                p=14400000

            if model_C == 9:
                c='BMW X4'
                print('CC-4395')
                print('BHP-261.49bhp@4000rpm')
                print('Torque-620Nm@2000-2500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -320kmph')
                print('Mileage-14kmpl')
                print('Tank capacity-65Litres')
                print('Seats-5')
                print('Price-71.90 - 73.90 Lakh')
                p=7390000

            if model_C == 10:
                c='BMW 7 SERIES'
                print('CC-2998')
                print('BHP-281.6bhp@5000-6000rpm')
                print('Torque-450Nm@1380-5000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-39.36Kmpl')
                print('Tank capacity-46Litres')
                print('Seats-4')
                print('Price-1.42 - 1.76 Cr')
                p=17600000

            if model_C == 11:
                c='BMW M2'
                print('CC-2998')
                print('BHP-410bhp@6250rpm')
                print('Torque-550Nm@2350-5230rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-10.53kmpl')
                print('Tank capacity-64Litres')
                print('Seats-5')
                print('Price-85.00 Lakh')
                p=8500000

            if model_C == 12:
                c='BMW X5 M'
                print('CC-2979')
                print('BHP-616.87bhp@6000rpm')
                print('Torque-750nm@1800-5600rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-10.63kmpl')
                print('Tank capacity-83Litres')
                print('Seats-4')
                print('Price-2.08 Cr')
                p=2080000

            if model_C == 13:
                c='BMW X1'
                print('CC-1995')
                print('BHP-187.74bhp@5000-6000rpm')
                print('Torque-400nm@1750-2500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-18.29kmpl')
                print('Tank capacity-51Litres')
                print('Seats-5')
                print('Price-41.50 - 44.50 Lakh')
                p=4450000

            if model_C == 14:
                c='BMW iX'
                print('CC-1998')
                print('BHP-321.84Bhp')
                print('Torque-630Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-19.62kmpl')
                print('Charging time-7.25hours')
                print('Seats-5')
                print('Price-1.16 Cr')
                p=11600000

            if model_C == 15:
                c='BMW i4'
                print('CC-2998')
                print('BHP-335.25bhp')
                print('Torque-430Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -190kmph')
                print('range- 493-590Km')
                print('battery capacity- 83.9Kw-')
                print('Seats-5')
                print('Price-69.90 Lakh')
                p=6990000

            if model_C == 16:
                c='BMW 6 SERIES'
                print('CC-2993')
                print('BHP-261.4bhp@4000rpm')
                print('Torque-620Nm@2000-2500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -230kmph')
                print('Mileage-17.09kmpl')
                print('Tank capacity-66Litres')
                print('Seats-4')
                print('Price-69.90 - 79.90 Lakhs')
                p=7990000

            if model_C == 17:
                c='BMW Z4'
                print('CC-2998')
                print('BHP-335bhp@5000-6500rpm')
                print('Torque-500Nm@1600-4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -230kmph')
                print('Mileage-14.37kmpl')
                print('Tank capacity-52Litres')
                print('Seats-4')
                print('Price-71.90 - 84.90 Lakh')
                p=8490000

            if model_C == 18:
                c='BMW 8 SERIES'
                print('CC-2998')
                print('BHP-600bhp@6000rpm')
                print('Torque-750nm@1800-5600rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-5.37kmpl')
                print('Tank capacity-68Litres')
                print('Seats-2')
                print('Price-1.62 - 2.23 Cr')
                p=22300000

            if model_C == 19:
                c='BMW X3 M'
                print('CC-2993')
                print('BHP-473.38bhp@6250rpm')
                print('Torque-600nm@2600-5600rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-9.3kmpl')
                print('Tank capacity-65Litres')
                print('Seats-4')
                print('Price-99.90 Lakh')
                p=9990000

            if model_C == 20:
                c='BMW iX1'
                print('CC-2993')
                print('BHP-187.74bhp@5000-6000rpm')
                print('Torque-400nm@1750-2500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -220kmph')
                print('Mileage-9.14kmpl')
                print('Tank capacity-74Litres')
                print('Seats-4')
                print('Price-60.00 Lakh')
                p=6000000

            if model_C == 21:
                c='BMW X1'
                print('CC-1995')
                print('BHP-187.74bhp@5000-6000rpm')
                print('Torque-400nm@1750-2500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -220kmph')
                print('Mileage-19.62kmpl')
                print('Tank capacity-51Litres')
                print('Seats-5')
                print('Price-41.50 - 44.50 Lakh')
                p=4450000

            if model_C == 22:
                c='BMW i7'
                print('CC-1998')
                print('BHP-257.47@rpm')
                print('Torque-289@rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-19.62kmpl')
                print('Tank capacity-85Litres')
                print('Seats-5')
                print('Price-2.50 Cr')
                p=25000000

            if model_C == 23:
                c='BMW i8'
                print('CC-1499')
                print('BHP-228bhp@5800rpm')
                print('Torque-320Nm@3700rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -220kmph')
                print('Mileage-47.45kmpl')
                print('Tank capacity-42Litres')
                print('Seats-4')
                print('Price-2.50Crore')
                p=25000000

            if model_C == 24:
                c='BMW M8'
                print('CC-4935')
                print('BHP-600bhp@6000rpm')
                print('Torque-750nm@1800-5600rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -220kmph')
                print('Mileage-5.59kmpl')
                print('Tank capacity-68Litres')
                print('Seats-4')
                print('Price-2.23Crore')
                p=22300000

            if model_C == 25:
                c='BMW M5'
                print('CC-4395cc')
                print('BHP-616.87bhp@6000rpm')
                print('Torque-750nm@1800-5860rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-9.12kmpl')
                print('Tank capacity-74Litres')
                print('Seats-5')
                print('Price-1.74Crore')
                p=17400000
                
            elif model_C < 1 or model_C > 25:
                print('Select the appropriate model ')
                cars()
        if a == 3:
            bb='BUGATTI'
            print('[1]BUGATTI VEYRON')
            print('[2]BUGATTI CHIRON')
            print('[3]BUGATTI DIVO')
            print('[4]BUGATTI CENTODIECI')
            print('[5]BUGATTI LA VOITURE NOIRE')
            print('[6]BUGATTI VISION GRANTURISMO')
            print('[7]BUGATTI BOLIDE')
            print('[8]BUGATTI VEYRON 16.4 SUPER SPORT')
            print('[9]BUGATTI CHIRON SUPER SPORT')
            print('[10]BUGATTI CHIRON PUR SPORT')
            print('[11]BUGATTI CHIRON SPORT')
            print('[12]BUGATTI CHIRON Les Légendes Du Ciel')
            print('[13]BUGATTI CHIRON EDITION NOIRE')
            print('[14]BUGATTI CHIRON SUPERSPORT 300+')
            print('[15]BUGATTI CHIRON 110 ANS')
            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='BUGATTI VEYRON'
                print('CC-7993')
                print('BHP-1001bhp@6000rpm')
                print('Torque-1250Nm@2200-5500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300kmph')
                print('Mileage-6kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-12Crore')
                p=120000000

            if model_C == 2:
                c='BUGATTI CHIRON'
                print('CC-7993')
                print('BHP-1600Nm@2000-6000rpm')
                print('Torque-1479bhp@6700rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300kmph')
                print('Mileage-6kmpl')
                print('Tank capacity-90Litres')
                print('Seats-2')
                print('Price-21Crore')
                p=210000000

            if model_C == 3:
                c='BUGATTI DIVO'
                print('CC-7993')
                print('BHP-1479bhp@6700rpm')
                print('Torque-1600Nm@2000-6000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -304kmph')
                print('Mileage-7kmpl')
                print('Tank capacity-90Litres')
                print('Seats-2')
                print('Price-41Crore')
                p=410000000

            if model_C == 4:
                c='BUGATTI CENTODIECI'
                print('CC-8000')
                print('BHP-1600 hp @ 7000 rpm')
                print('Torque-1180 ft-lb')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -236mph')
                print('Mileage-7kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-66Crores')
                p=660000000

            if model_C == 5:
                c='BUGATTI LA VOITURE NOIRE'
                print('CC-7993')
                print('BHP-1500 PS @ 6700rpm')
                print('Torque-1600 Nm @ 2000 - 6000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-7kmpl')
                print('Tank capacity-90Litres')
                print('Seats-2')
                print('Price-98Crore')
                p=980000000

            if model_C == 6:
                c='BUGATTI VISION GRANTURISMO'
                print('CC-7993')
                print('BHP-1,479 BHP @ around 6,700 rpm')
                print('Torque- 1,600 Nm @ 2,000 - 6,000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -280kmph')
                print('Mileage-7.6kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-21Crore')
                p=210000000

            if model_C == 7:
                c='BUGATTI BOLIDE'
                print('CC-1451')
                print('BHP-1,177 kW (1,578 hp; 1,600 PS)')
                print('Torque-1,600 N⋅m (1,180 lbf⋅ft) at 2,250 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-9kmpl')
                print('Tank capacity-75Litres')
                print('Seats-2')
                print('Price-19.21Crore')
                p=192100000

            if model_C == 8:
                c='BUGATTI VEYRON 16.4 SUPER SPORT'
                print('CC-7993')
                print('BHP-987 bhp @ 6000 rpm ')
                print('Torque-1250 Nm @ 2200 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -280kmph')
                print('Mileage-9.3kmpl')
                print('Tank capacity-90Litres')
                print('Seats-2')
                print('Price- ₹ 11.39 Crore')
                p=113900000

            if model_C == 9:
                c='BUGATTI CHIRON SUPER SPORT'
                print('CC-7993')
                print('BHP-1479bhp@6700rpm')
                print('Torque-1600Nm@2000-6000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -280kmph')
                print('Mileage-7kmpl')
                print('Tank capacity-90Litres')
                print('Seats-2')
                print('Price-19.21Crores')
                p=192100000

            if model_C == 10:
                c='BUGATTI CHIRON PUR SPORT'
                print('CC-7993')
                print('BHP-1479 BHp ps ')
                print('Torque-1600 N·m1180 lb·ft')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-7kmpl')
                print('Tank capacity-75Litres')
                print('Seats-2')
                print('Price-21Crore')
                p=210000000

            if model_C == 11:
                c='BUGATTI CHIRON SPORT'
                print('CC-7993')
                print('BHP-1479 bhp @ 6700 rpm')
                print('Torque-1600Nm@2000-6000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -280kmph')
                print('Mileage-7.9kmpl')
                print('Tank capacity-75Litres')
                print('Seats-2')
                print('Price-21Crore')
                p=210000000

            if model_C == 12:
                c='BUGATTI CHIRON Les Légendes Du Ciel'
                print('CC-7993')
                print('BHP- 1,500 PS')
                print('Torque-1600Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-21Crore')
                p=210000000

            if model_C == 13:
                c='BUGATTI CHIRON EDITION NOIRE'
                print('CC-7993')
                print('BHP-@rpm 1,103 kW (1,479 hp; 1,500 PS) ')
                print('Torque-1,600 N⋅m (1,180 lb⋅ft)')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300kmph')
                print('Mileage-5Litres')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-21Crore')
                p=210000000

            if model_C == 14:
                c='BUGATTI CHIRON SUPERSPORT 300+'
                print('CC-7993')
                print('BHP-1,577 hp @ 7,000 rpm (1,176 kW)')
                print('Torque-1,180 lb·ft @ 2,000 – 6,000 rpm (1,600 N·m)')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-92Crore')
                p=920000000

            if model_C == 15:
                c='BUGATTI CHIRON 110 ANS'
                print('CC-7993')
                print('BHP-1,479 hp @ 6,900 rpm (1,103 kW)')
                print('Torque-1,180 lb·ft @ 2,000 – 6,000 rpm (1,600 N·m)')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -320kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-106Crore')
                p=106000000
           
            elif model_C < 1 or model_C > 15:
                print('Select the appropriate model ')
                cars()
        if a == 4:
            bb='DEVEL SIXTEEN'
            print('[1]DEVEL SIXTEEN V16')
            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='DEVEL SIXTEEN V16'
                print('CC-12300')
                print('BHP-5007 HP')
                print('Torque-5090 Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -500kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-44.96Crore')
                p=449600000

            elif model_C < 1 or model_C > 1:
                print('Select the appropriate model ')
                cars()
        if a == 5:
            bb='HONDA'
            print('[1]HONDA CITY')
            print('[2]HONDA AMAZE')
            print('[3]HONDA JAZZ')
            print('[4]HONDA CIVIC')
            print('[5]HONDA CIVIC TYPE R')
            print('[6]HONDA CR V')
            print('[7]HONDA BR V')
            print('[8]HONDA WR V')
            print('[9]HONDA HR V')
            print('[10]HONDA CITY HYBRID EHEV')
            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C ==1:
                c='HONDA CITY'
                print('CC-1498')
                print('BHP-97.89bhp@3600rpm')
                print('Torque-200Nm@1750rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -195kmph')
                print('Mileage-15.32kmpl')
                print('Tank capacity-40L')
                print('Seats-5')
                print('Price-11.57-15.52Lakhs')
                p=1552000
            
            if model_C ==2:
                c='HONDA AMAZE'
                print('CC-1498')
                print('BHP-79.12bhp@3600rpm')
                print('Torque-160Nm@1750rpm')
                print('TRANSMISSION-Automatic/Manual')
                print('TOP SPEED -160kmph')
                print('Mileage-24.7kmpl')
                print('Tank capacity-35Litres')
                print('Seats-5')                     
                print('Price-6.63 - 11.50 Lakh')
                p=1150000
            
            if model_C ==3:
                c='HONDA JAZZ'
                print('CC-1199')
                print('BHP-88.50bhp@6000rpm')
                print('Torque-110Nm@4800rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -172kmph')
                print('Mileage-17.1kmpl')
                print('Tank capacity-40')
                print('Seats-5')                     
                print('Price-Rs.8.01 - 10.32 Lakh')
                p=1032000
            
            if model_C ==4:
                c='HONDA CIVIC'
                print('CC-1799')
                print('BHP-139@6500rpm')
                print('Torque-174@4300rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -270kmph')
                print('Mileage-16.5kmpl')
                print('Tank capacity-47')
                print('Seats-5')
                print('Price-15.00 Lakh - 22.35 Lakh')
                p=2235000
            
            if model_C ==5:
                c='HONDA CIVIC TYPE R'
                print('CC-1996')
                print('BHP-217@8000rpm')
                print('Torque-295 lb-ft @ 2500-4500 rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -261kmph')
                print('Mileage-26.8kmpl')
                print('Tank capacity-47Litres')
                print('Seats-5')
                print('Price-58Lakh')
                p=5800000
            
            if model_C ==6:
                c='HONDA CR V'
                print('CC-1997')
                print('BHP-151.89bhp@6500rpm')
                print('Torque-189NM@4300rpm')
                print('TRANSMISSION- Automatic')
                print('TOP SPEED - 195kmph')
                print('Mileage-14.4 kmpl')
                print('Tank capacity-57Litres')
                print('Seats-5')                     
                print('Price-21.10 Lakh - 32.77 Lakh')
                p=3277000
            
            if model_C ==7:
                c='HONDA BR V'
                print('CC-1497')
                print('BHP-117.3bhp@6600rpm')
                print('Torque-145Nm@4600rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -')
                print('Mileage-15.4kmpl')
                print('Tank capacity-42Litres')
                print('Seats-7')
                print('Price-9.53 Lakh - 13.83 Lakh')
                p=1383000
            
            if model_C ==8:
                c='HONDA WR V'
                print('CC-1498')
                print('BHP-88.7bhp@6000rpm')
                print('Torque-110Nm@4800rpm')
                print('TRANSMISSION- Manual')
                print('TOP SPEED -176kmph')
                print('Mileage-17.5kmpl')
                print('Tank capacity-40Litres')
                print('Seats-5')
                print('Price-8.08 Lakh - 10.48 Lakh')
                p=1048000
            
            if model_C ==9:
                c='HONDA HR V'
                print('CC-1198')
                print('BHP-@rpm')
                print('Torque-@rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -')
                print('Mileage-')
                print('Tank capacity-')
                print('Seats-5')
                print('Price-14.00 Lakh')
                p=1400000
            
            if model_C ==10:
                c='HONDA CITY HYBRID EHEV'
                print('CC-1498')
                print('BHP-96.55bhp@5600-6400rpm')
                print('Torque-127nm@4500-5000')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -170kmph')
                print('Mileage-26.5kmpl')
                print('Tank capacity-40Litres')
                print('Seats-5')
                print('Price-19.89 Lakh')
                p=1989000
                     
            elif model_C < 1 or model_C >10:
                    print('Select the appropriate model ')
                    cars()


        if a == 6:
            bb='HYUNDAI'
            print('[1] HYUNDAI ELENTRA')
            print('[2] HYUNDAI STARGAZER')
            print('[3] HYUNDAI CASPER')
            print('[4] HYUNDAI CRETA')
            print('[5] HYUNDAI KONA')
            print('[6] HYUNDAI i10 grandnios')
            print('[7] HYUNDAI i20')
            print('[8] HYUNDAI AURA')
            print('[9] HYUNDAI VERNA')
            print('[10] HYUNDAI VENUE')
            print('[11] HYUNDAI TUCRON')
            print('[12] HYUNDAI SANTRO')
            print('[13] HYUNDAI ALCAZAR')
            print('[14] HYUNDAI i20 N LINE')
            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C ==1:
                c='HYUNDAI ELENTRA'
                print('CC-1582')
                print('BHP-126.2bhp@4000rpm')
                print('Torque-259.88Nm@1900-2750rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -150kmph')
                print('Mileage-14.59kmpl')
                print('Tank capacity-50Litres')
                print('Seats-5')
                print('Price-15.00- 21.13 Lakh')
                p=2113000
            if model_C ==2:
                c='HYUNDAI STARGAZER'
                print('CC-1499')
                print('BHP-116.2bhp@4000rpm')
                print('Torque-259.88Nm@1900-2750rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -180kmph')
                print('Mileage-11kmpl')
                print('Tank capacity-50L')
                print('Seats-4')
                print('Price-10.00 Lakh')
                p=1000000
            if model_C ==3:
                c='HYUNDAI CASPER'
                print('CC-999')
                print('BHP-116.2bhp@4000rpm')
                print('Torque-259.88Nm@1900-2750rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -160kmph')
                print('Mileage-12.4kmpl')
                print('Tank capacity-60L')
                print('Seats-5')
                print('Price-6.00Lakhs')
                p=600000
            if model_C ==4:
                c='HYUNDAI CRETA'
                print('CC-1493')
                print('BHP-113.45bhp@4000rpm')
                print('Torque-250nm@1500-2750rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -150kmpl')
                print('Mileage-18kmpl')
                print('Tank capacity-50Litres')
                print('Seats-5')
                print('Price-10.44 - 18.18 Lakh')
                p=1818000
            if model_C ==5:#electric
                c='HYUNDAI KONA'
                print('CC-1493')
                print('BHP-134.10bhp')
                print('Torque-395Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -160kmpl')
                print('Mileage-14.3kmpl')
                print('charging time- Approx 6 h 10 min')
                print('Seats-5')
                print('Price-23.84 - 24.03 Lakh')
                p=2403000
            if model_C ==6:
                c='HYUNDAI i10 grandnios'
                print('CC-1197')
                print('BHP-81.86bhp@6000rpm')
                print('Torque-113.8nm@4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -150kmph')
                print('Mileage-20.7kmpl')
                print('Tank capacity-37Litres')
                print('Seats-5')
                print('Price-5.39 - 8.02 Lakh')
                p=802000
            if model_C ==7:
                c='HYUNDAI i20'
                print('CC-1493')
                print('BHP-118.36bhp@6000rpm')
                print('Torque-171.62nm@1500-4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -175kmph')
                print('Mileage-20.28kmpl')
                print('Tank capacity-37Litres')
                print('Seats-5')
                print('Price-7.03 - 11.54 Lakh')
                p=1154000
            if model_C ==8:
                c='HYUNDAI AURA'
                print('CC-1197')
                print('BHP-98.63bhp@6000rpm')
                print('Torque-172nm@1500-4000rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -150kmph')
                print('Mileage-20.5kmpl')
                print('Tank capacity-37Litres')
                print('Seats-5')
                print('Price-6.09 - 8.87 Lakh')
                p=887000
            if model_C ==9:
                c='HYUNDAI VERNA'
                print('CC-1497')
                print('BHP-113.45bhp@4000rpm')
                print('Torque-250Nm@1500-2750rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -140kmph')
                print('Mileage-21.3kmpl')
                print('Tank capacity-45Litres')
                print('Seats-5')
                print('Price-9.41 - 15.45 Lakh')
                p=1545000
            if model_C ==10:
                c='HYUNDAI VENUE'
                print('CC-998')
                print('BHP-118.41bhp@6000rpm')
                print('Torque-172Nm@1500-4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -160kmph')
                print('Mileage-16.0kmpl(city)')
                print('Tank capacity-45Litres')
                print('Seats-5')
                print('Price-7.53 - 12.72 Lakh')
                p=1272000
            if model_C ==11:
                c='HYUNDAI TUCRON'
                print('CC-1997')
                print('BHP-183.72bhp@4000rpm')
                print('Torque-416nm@2000-2750rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -150kmph')
                print('Mileage-15kmpl')
                print('Tank capacity-60L')
                print('Seats-5')
                print('Price-27.70 - 34.54 Lakh')
                p=3454000
            if model_C ==12:
                c='HYUNDAI SANTRO'
                print('CC-1086')
                print('BHP-59.17bhp@5500rpm')
                print('Torque-85.3Nm@4500 rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -180kmph')
                print('Mileage-30.48kmpl')
                print('Tank capacity-60Litres')
                print('Seats-5')
                print('Price-4.90 - 6.42 Lakh')
                p=642000
            if model_C ==13:
                c='HYUNDAI ALCAZAR'
                print('CC-1999')
                print('BHP-113.42bhp@4000rpm')
                print('Torque-250nm@1500-2750rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -180kmph')
                print('Mileage-18.1kmpl')
                print('Tank capacity-50Litres')
                print('Seats-7')
                print('Price-15.89 - 20.25 Lakh')
                p=2025000
            if model_C ==14:
                c='HYUNDAI i20 N LINE'
                print('CC-998')
                print('BHP-118.41bhp@6000rpm')
                print('Torque-172nm@1500-4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -150kmpl')
                print('Mileage-20.25kmpl')
                print('Tank capacity-37Litres')
                print('Seats-5')
                print('Price-9.96 - 12.02 Lakh')
                p=1204000
            elif model_C < 1 or model_C > 14:
                print('Select the appropriate model ')
                cars()
        if a == 7:
            bb='LAMBORGHINI'
            print('[1]LAMBORGHINI URUS')
            print('[2]LAMBORGHINI HURACAN EVO')
            print('[3]LAMBORGHINI AVENTADOR')
            print('[4]LAMBORGHINI HURACAN STO')
            print('[5]LAMBORGHINI HURACAN EVO RWD')
            print('[6]LAMBORGHINI SESTO ELEMENTO')
            print('[7]LAMBORGHINI AVENTADOR J')
            print('[8]LAMBORGHINI SIAN')
            print('[9]LAMBORGHINI VENENO')
            print('[10]LAMBORGHINI VENENO ROADSTER')
            print('[11]LAMBORGHINI SAIN ROADSTER')
            print('[12]LAMBORGHINI CENTENARIO')
            print('[13]LAMBORGHINI CENTENARIO ROADSTER')
            print('[14]LAMBORGHINI SCL8 ALSTON')
            print('[15]LAMBORGHINI ESSENZA SCUR')
            print('[16]LAMBORGHINI SCJ')
            print('[17]LAMBORGHINI DIABLO')
            print('[18]LAMBORGHINI COUNTACH')
            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='LAMBORGHINI URUS'
                print('CC-3996 cc')
                print('BHP-650 bhp @ 6000 rpm')
                print('Torque-850 Nm @ 2250 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -305 Kmph')
                print('Mileage-7.8kmpl')
                print('Tank capacity-100L')
                print('Seats-4')
                print('Price-3.10Crore')
                p=31000000

            if model_C == 2:
                c='LAMBORGHINI HURACAN EVO'
                print('CC-5204')
                print('BHP-630.28bhp@8000rpm')
                print('Torque-565Nm@6500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -325kmph')
                print('Mileage-7.25kmpl')
                print('Tank capacity-85L')
                print('Seats-2')
                print('Price-3.21 - 4.99 Cr')
                p=49900000

            if model_C == 3:
                c='LAMBORGHINI AVENTADOR'
                print('CC-6498')
                print('BHP-740 CV (544 kW) @ 8.400 rpm')
                print('Torque-690 Nm (507 lb.-ft.) @ 5.500 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -350kmph')
                print('Mileage-3.22Kmpl')
                print('Tank capacity-90L')
                print('Seats-2')
                print('Price-6.25 - 9.00 Cr')
                p=90000000

            if model_C == 4:
                c='LAMBORGHINI HURACAN STO'
                print('CC-5204 cc')
                print('BHP-858 bhp@8000 rpm')
                print('Torque-565 Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -310kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-90L')
                print('Seats-2')
                print('Price-4.99 Crore')
                p=49900000

            if model_C == 5:
                c='LAMBORGHINI HURACAN EVO RWD'
                print('CC-5204')
                print('BHP-610bhp')
                print('Torque-560Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -350kmph')
                print('Mileage-4kmpl')
                print('Tank capacity-90L')
                print('Seats-2')
                print('Price-3.21 Cr')
                p=32100000

            if model_C == 6:
                c='LAMBORGHINI SESTO ELEMENTO'
                print('CC-5204')
                print('BHP-570bhp')
                print('Torque-400Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED - 350kmph')
                print('Mileage-5kmpl')
                print('Tank capacity- 100L')
                print('Seats-2')
                print('Price- 5.01 Crore - ₹ 5.62 Crore')
                p=56200000

            if model_C == 7:
                c='LAMBORGHINI AVENTADOR J'
                print('CC-5204')
                print('BHP-425.77 bhp per tonne')
                print('Torque-690 nm / 508.9 ft lbs @ 5500 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -350kmph')
                print('Mileage-5.5kmpl')
                print('Tank capacity-100L')
                print('Seats-2')
                print('Price-4Crore')
                p=40000000

            if model_C == 8:
                c='LAMBORGHINI SIAN'
                print('CC-5204')
                print('BHP-819 CV (602 kW) @ 8,500 rpm')
                print('Torque-720 Nm @ 6750 rpm.')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -380kmph')
                print('Mileage-4kmpl')
                print('Tank capacity-100L')
                print('Seats-2')
                print('Price-₹ 3.05 - ₹ 4.99 Crore')
                p=49900000

            if model_C == 9:
                c='LAMBORGHINI VENENO'
                print('CC-6498')
                print('BHP-750 CV (552 kW) @ 8.400 rpm')
                print('Torque-690 Nm (507 lb.-ft.) @ 5.500 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -380kmph')
                print('Mileage-4.7kmpl')
                print('Tank capacity-90L')
                print('Seats-2')
                print('Price- 27.72 crore')
                p=277200000

            if model_C == 10:
                c='LAMBORGHINI VENENO ROADSTER'
                print('CC-6498 cc')
                print('BHP- 750 PS (552 kW; 740 hp) at 8,400 rpm')
                print('Torque-690 N⋅m (509 lb⋅ft) of torque at 5,500 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -355kmph')
                print('Mileage-4.4kmpl')
                print('Tank capacity-90L')
                print('Seats-2')
                print('Price- 27.72 crore')
                p=277200000

            if model_C == 11:
                c='LAMBORGHINI SAIN ROADSTER'
                print('CC-6498')
                print('BHP-785 PS (774 bhp - 577 kW) at 8500 rpm')
                print('Torque-720 Nm (531 lb. ft) at 6750 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -355kmph')
                print('Mileage-5.1kmpl')
                print('Tank capacity-90L')
                print('Seats-2')
                print('Price-Rs 29.4 Crore')
                p=294000000

            if model_C == 12:
                c='LAMBORGHINI CENTENARIO'
                print('CC-6498')
                print('BHP-770 CV (566 kW) @ 8.500 rpm')
                print('Torque- 690 N⋅m (509 lb⋅ft) of torque at 5,500 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -355kmph')
                print('Mileage-5.2kmpl')
                print('Tank capacity-100L')
                print('Seats-2')
                print('Price-15.4 crore')
                p=154000000

            if model_C == 13:
                c='LAMBORGHINI CENTENARIO ROADSTER'
                print('CC-6498')
                print('BHP-770 CV (566 kW) @ 8.500 rpm')
                print('Torque-@rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -380kmph')
                print('Mileage-4.4kmpl')
                print('Tank capacity-85L')
                print('Seats-2')
                print('Price-15.4 crore')
                p=154000000

            if model_C == 14:
                c='LAMBORGHINI SCL8 ALSTON'
                print('CC-6498')
                print('BHP- 770 HP @ 8,500 RPM')
                print('Torque-531 LB-FT @ 6,750 RPM')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -350kmpl')
                print('Mileage-4.2kmpl')
                print('Tank capacity-90L')
                print('Seats-2')
                print('Price-20Crore')
                p=200000000

            if model_C == 15:
                c='LAMBORGHINI ESSENZA SCUR'
                print('CC-6498')
                print('BHP-610 kW (830 PS; 820 hp)')
                print('Torque-560lb ft of torque at 7,000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -350kmph')
                print('Mileage-77kmpl')
                print('Tank capacity-80L')
                print('Seats-2')
                print('Price-25Crore')
                p=250000000

            if model_C == 16:
                c='LAMBORGHINI SCJ'
                print('CC-5204')
                print('BHP-566 kW (770 CV) at 8,500 rpm')
                print('Torque- 720 Nm of torque at 6,750 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -350kmpl')
                print('Mileage-7kmpl')
                print('Tank capacity-90L')
                print('Seats-2')
                print('Price-6.5Crore')
                p=65000000

            if model_C == 17:
                c='LAMBORGHINI DIABLO'
                print('CC-3929')
                print('BHP-492 PS (362 kW; 485 hp)')
                print('Torque-580 N⋅m (428 lbf⋅ft)')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -355kmph')
                print('Mileage-4.7kmpl')
                print('Tank capacity-85L')
                print('Seats-2')
                print('Price-1.48 crore and Rs 1.68 Crore')
                p=16800000

            if model_C == 18:
                c='LAMBORGHINI COUNTACH'
                print('CC-3929')
                print('BHP-814 CV (599 kW) @ 8,500 rpm')
                print('Torque-268 lbft / 5500 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300kmph')
                print('Mileage-7kmpl')
                print('Tank capacity-75L')
                print('Seats-2')
                print('Price-20Crores')
                p=200000000

            elif model_C < 1 or model_C > 18:
                print('Select the appropriate model ')
                cars()
        if a == 8:
            bb='Koenigsegg'
            print('[1]Koenigsegg Regera ')
            print('[2]Koenigsegg Jesko ')
            print('[3]Koenigsegg Gemera ')
            print('[4]Koenigsegg Jesko Absolut')
            print('[5]Koenigsegg Agera R')
            print('[6]Koenigsegg Agera')
            print('[7]Koenigsegg Agera S ')
            print('[8]Koenigsegg Agera RS')
            print('[9]Koenigsegg One:1 ')

            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='Koenigsegg Regera'
                print('CC-4695')
                print('BHP-1100@7800rpm')
                print('Torque-1280NM@4100rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -255 mph')
                print('Mileage-6kmph')
                print('Tank capacity-80litres')
                print('Seats-2')
                print('Price-30Crores')
                p=300000000

            if model_C == 2:
                c='Koenigsegg Jesko'
                print('CC-5,065.48 ')
                print('BHP-1578BHP @ 7800 RPM')
                print('Torque-1500Nm @ 5100 RPM')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -380mph')
                print('Mileage-5kmpl')
                print('Tank capacity-85Litres')
                print('Seats-2')
                print('Price-21Crore')
                p=210000000

            if model_C == 3:
                c='Koenigsegg Gemera'
                print('CC-1988.25cc')
                print('BHP- 600 bhp at 7500 rpm')
                print('Torque-600 Nm from 2000 rpm to 7000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -270kmph')
                print('Mileage-4kmpl')
                print('Tank capacity-75Litres')
                print('Seats-2')
                print('Price-13Crore')
                p=130000000


            if model_C == 4:
                c='Koenigsegg Jesko Absolut'
                print('CC-5065')
                print('BHP-955 kW (1,298 PS; 1,281 hp) at 7800 rpm')
                print('Torque-,000 N⋅m (738 lb⋅ft) of torque at 2700 to 6170 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -280kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-85Litres')
                print('Seats-2')
                print('Price-19.05Crore')
                p=190500000

            if model_C == 5:
                c='Koenigsegg Agera R'
                print('CC-5065')
                print('BHP-1124 hp @ 7100 rpm')
                print('Torque-885 lb-ft @ 4100 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300kmph')
                print('Mileage-5.12kmpl')
                print('Tank capacity-75Litres')
                print('Seats-2')
                print('Price-12.5Crore')
                p=125000000

            if model_C == 6:
                c='Koenigsegg Agera'
                print('CC-4905')
                print('BHP-910 Bhp @ 6850 rpm')
                print('Torque-1100 Nm @ 5100 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -390Kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-70Litres')
                print('Seats-2')
                print('Price-12Crore')
                p=120000000

            if model_C == 7:
                c='Koenigsegg Agera S'
                print('CC-4695')
                print('BHP-1030 hp @ 7100 rpm')
                print('Torque-811 lb-ft @ 4100 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -273kmph')
                print('Mileage-8kmpl')
                print('Tank capacity-80Litres')
                print('Seats-2')
                print('Price-12Crore')
                p=120000000

            if model_C == 8:
                c='Koenigsegg Agera RS'
                print('CC-5065')
                print('BHP-1,160 hp @ 7,800 rpm (865 kW)')
                print('Torque-944 lb·ft @ 4,100 rpm (1,280 N·m)')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300kmph')
                print('Mileage-7kmpl')
                print('Tank capacity-150Litres')
                print('Seats-2')
                print('Price-13Crore')
                p=130000000

            if model_C == 9:
                c='Koenigsegg One:1'
                print('CC-5065')
                print('BHP-7500 rpm – rpm limiter @ 8250 rpm')
                print('Torque-1000 Nm from 3000 to 8000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -320kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-80Litres')
                print('Seats-2')
                print('Price-40Crore')
                p=400000000

            elif model_C < 1 or model_C > 9:
                print('Select the appropriate model ')
                cars()
        if a == 9:
            bb='Mercedes Benz'
            print('[01]Mercedes Benz EQS')
            print('[02]Mercedes Benz G-CLASS')
            print('[03]Mercedes Benz C-CLASS')
            print('[04]Mercedes Benz GLA')
            print('[05]Mercedes Benz MAYBACH S-CLASS')
            print('[06]Mercedes Benz A CLASS LIMOUSINE')
            print('[07]Mercedes Benz GLS')
            print('[08]Mercedes Benz E-CLASS')
            print('[09]Mercedes Benz MAYBACH GLS')
            print('[10]Mercedes Benz GLC')
            print('[11]Mercedes Benz  CLASS CARBRIOTET')
            print('[12]Mercedes Benz AMG 35')
            print('[13]Mercedes Benz AMGGLA 3T')
            print('[14]Mercedes Benz GLC COUPE')
            print('[15]Mercedes Benz AMG GT 4 DOOR COUPE')
            print('[16]Mercedes Benz AMG GLE coupe')
            print('[17]Mercedes Benz AMG e63')
            print('[18]Mercedes Benz EQC')
            print('[19]Mercedes Benz AMGE 53')
            print('[20]Mercedes Benz AMGA 45S')
            print('[21]Mercedes Benz EQE')
            print('[22]Mercedes Benz EQB')

            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='Mercedes Benz EQS'
                print('BHP-750.97bhp')
                print('Torque-1020Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('range-526-580km')
                print('Seats-5')
                print('Price-2.54 Cr')
                p=25400000

            if model_C == 2:
                c='Mercedes Benz G-CLASS'
                print('CC-2925')
                print('BHP-281.61bhp@3400-4600rpm')
                print('Torque-600Nm@1200-3200rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -200kmph')
                print('Mileage-15kmpl')
                print('Tank capacity-100Litres')
                print('Seats-5')
                print('Price-1.72 Cr')
                p=17200000

            if model_C == 3:
                c='Mercedes Benz C-CLASS'
                print('CC-1993')
                print('BHP-261.49bhp@4200rpm')
                print('Torque-550nm@1800-2200rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -220kmph')
                print('Mileage-20kmpl')
                print('Tank capacity- 64litres')
                print('Seats-5')
                print('Price-55.00 - 61.00 Lakh')
                p=6100000

            if model_C == 4:
                c='Mercedes Benz GLA'
                print('CC-1950')
                print('BHP-187.74bhp@3800rpm')
                print('Torque-400Nm@1600-2600rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -230kmph')
                print('Mileage-15kmpl')
                print('Tank capacity-')
                print('Seats-5')
                print('Price-44.90 - 48.90 Lakh')
                p=4890000

            if model_C == 5:
                c='Mercedes Benz MAYBACH S-CLASS'
                print('CC-5980')
                print('BHP-603.46bhp@5250-5500')
                print('Torque-900nm@2000-4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250 kmph')
                print('Mileage-7.5-9.8kmpl')
                print('Tank capacity-76litres')
                print('Seats-5')
                print('Price-2.50 - 3.20 Cr')
                p=32000000

            if model_C == 6:
                c='Mercedes Benz A CLASS LIMOUSINE'
                print('CC-1950')
                print('BHP-147.51bhp@1620-4000rpm')
                print('Torque-320Nm@1400-3500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -227kmph')
                print('Mileage-17.5 kmpl ')
                print('Tank capacity-43Litres')
                print('Seats-4')
                print('Price-42.00 - 44.00 Lakh')
                p=4400000

            if model_C == 7:
                c='Mercedes Benz GLS'
                print('CC-3982')
                print('BHP-549.81bhp-6500rpm')
                print('Torque-730nm@2500-4500rpm')
                print('TRANSMISSION-Autoamtic')
                print('TOP SPEED -222 kmph')
                print('Mileage-12.5kmpl')
                print('Tank capacity-90Litres')
                print('Seats-7')
                print('Price-1.16 - 2.47 Cr')
                p=24700000

            if model_C == 8:
                c='Mercedes Benz E-CLASS'
                print('CC-2925')
                print('BHP-281.61bhp@3400-4600rpm')
                print('Torque-600nm@1200-3200rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250 Kmph.')
                print('Mileage-12.06kmpl')
                print('Tank capacity-66Litres')
                print('Seats-5')
                print('Price-67.00 - 85.00 Lakh')
                p=8500000

            if model_C == 9:
                c='Mercedes Benz MAYBACH GLS'
                print('CC-3982')
                print('BHP-549.81bhp-6500rpm')
                print('Torque-730nm@2500-4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300 kmph')
                print('Mileage-8.5kmpl')
                print('Tank capacity- 90Litres')
                print('Seats-7')
                print('Price-1.16 - 2.47 Cr')
                p=24700000

            if model_C == 10:
                c='Mercedes Benz GLC'
                print('CC-1950')
                print('BHP-194bhp@3800rpm')
                print('Torque-400nm@2800rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -215kmph')
                print('Mileage-15kmpl')
                print('Tank capacity-66Litres')
                print('Seats-5')
                print('Price-62.00 - 68.00 Lakh')
                p=6800000

            if model_C == 11:
                c='Mercedes Benz  CLASS CARBRIOTET'
                print('CC-1991')
                print('BHP- 255@5800rpm')
                print('Torque-370 Nm @ 1800 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250 Kmph')
                print('Mileage-11kmpl')
                print('Tank capacity-50Litres')
                print('Seats-4')
                print('Price-70.64 Lakh')
                p=7064000

            if model_C == 12:
                c='Mercedes Benz AMG 35'
                print('CC-1991')
                print('BHP-301 bhp @ 5800 rpm')
                print('Torque-400 Nm @ 3000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED - 250 Kmph.')
                print('Mileage-13.3kmpl')
                print('Tank capacity-51Litres')
                print('Seats-5')
                print('Price-58Lakh')
                p=5800000

            if model_C == 13:
                c='Mercedes Benz AMGGLA 3T'
                print('CC-1991 cc')
                print('BHP-301.73bhp@5800rpm')
                print('Torque-400nm@3000-4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-15kmpl')
                print('Tank capacity-50Litres')
                print('Seats-5')
                print('Price-1.5Crore')
                p=15000000

            if model_C == 14:
                c='Mercedes Benz GLC COUPE'
                print('CC-1991')
                print('BHP-241.38bhp@4200rpm')
                print('Torque-500nm@1600-2400rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -240kmph')
                print('Mileage-12.7kmpl')
                print('Tank capacity-66Litres')
                print('Seats-5')
                print('Price-72.50 - 73.50 Lakh')
                p=7350000

            if model_C == 15:
                c='Mercedes Benz AMG GT 4 DOOR COUPE'
                print('CC-3998')
                print('BHP-639bhp')
                print('Torque-900nm@2500-4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -177 mph')
                print('Mileage-8.8 kmpl')
                print('Tank capacity-65 litres')
                print('Seats-4')
                print('Price-2.70 Cr')
                p=27000000

            if model_C == 16:
                c='Mercedes Benz AMG GLE coupe'
                print('CC-2996 cc')
                print('BHP- 362 bhp @ 5500 rpm.')
                print('Torque- 520 Nm @ 2000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -155kmph')
                print('Mileage-12kmpl')
                print('Tank capacity-85Litres')
                print('Seats-4')
                print('Price-2Crore')
                p=20000000

            if model_C == 17:
                c='Mercedes Benz AMG e63'
                print('CC-3982cc')
                print('BHP- 604 bhp @ 5750 rpm')
                print('Torque- 850 Nm @ 2500 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300 Kmph')
                print('Mileage-8.6kmpl')
                print('Tank capacity-66Litres')
                print('Seats-5')
                print('Price-1.7Crore')
                p=17000000

            if model_C == 18:
                c='Mercedes Benz EQC'
                print('BHP-402.30Bhp')
                print('Torque-760Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -180kmph')
                print('Mileage-11kmpl')
                print('battery capacity-41 Hrs @ 220 Volt')
                print('Seats-5')
                print('Price-1Crore')
                p=10000000

            if model_C == 19:# check it
                c='Mercedes Benz AMGE 53'
                print('CC-3982cc')
                print('BHP- 604 bhp @ 5750 rpm')
                print('Torque- 850 Nm @ 2500 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300 Kmph')
                print('Mileage-8.6kmpl')
                print('Tank capacity-66Litres')
                print('Seats-5')
                print('Price-1.7Crore')
                p=17000000

            if model_C == 20:
                c='Mercedes Benz AMGA 45S'
                print('CC-1991')
                print('BHP-421 bhp @ 6750 rpm')
                print('Torque-500 Nm @ 5000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -270 kmph')
                print('Mileage-12 kmpl')
                print('Tank capacity-51Litres')
                print('Seats-4')
                print('Price-81.50 Lakh')
                p=8150000

            if model_C == 21:
                c='Mercedes Benz EQE'
                print('BHP-215 kW (292 PS)')
                print('Torque-565 Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -210kmph')
                print('Range-525km')
                print('Battery capacity- 100kWh')
                print('Seats-5')
                print('Price-70Lakhs')
                p=7000000

            if model_C == 22:
                c='Mercedes Benz EQB'
                print('BHP-215 kW (292 PS)')
                print('Torque-520Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -160kmph')
                print('Range-330 km')
                print('Battery capacity- 69.7 kWh')
                print('Seats-7')
                print('Price-50Lakhs')
                p=5000000

            elif model_C < 1 or model_C > 22:
                print('Select the appropriate model ')
                cars()
        if a == 10:
            bb='NISSAN'
            print('[1]NISSAN GTR')
            print('[2]NISSAN KICK')
            print('[3]NISSAN MAGNITE')
            print('[4]NISSAN X TRAIL')
            print('[5]NISSAN X TRAIL HYBRID')
            print('[6]NISSAN SUNNY')
            print('[7]NISSAN MICRA ACTIVE')
            print('[8]NISSAN MICRA')
            print('[9]NISSAN TERRANO')
            print('[10]NISSAN PATROL')
            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='NISSAN GTR'
                print('CC-3798')
                print('BHP-562.20bhp@6800rpm')
                print('Torque-637Nm@3300-5800rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -350kmph')
                print('Mileage-9.0kmpl')
                print('Tank capacity-74Litres')
                print('Seats-4')
                print('Price-2.12 Cr')
                p=21200000

            if model_C == 2:
                c='NISSAN KICK'
                print('CC-1498')
                print('BHP-153.87bhp@5500rpm')
                print('Torque-254nm@1600rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -130kmph')
                print('Mileage-14.23kmpl')
                print('Tank capacity-50Litres')
                print('Seats-5')
                print('Price-9.50 - 14.90 Lakh')
                p=1490000

            if model_C == 3:
                c='NISSAN MAGNITE'
                print('CC-999')
                print('BHP-98.63bhp@5000rpm')
                print('Torque-152nm@2200-4400rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -160kmph')
                print('Mileage-17.7kmpl')
                print('Tank capacity-40Litres')
                print('Seats-5')
                print('Price-5.97 - 10.79 Lakh')
                p=1079000

            if model_C == 4:
                c='NISSAN X TRAIL'
                print('CC-1995')
                print('BHP-142bhp@4000rpm')
                print('Torque-200Nm@2000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -180kmph')
                print('Mileage-11kmpl')
                print('Tank capacity-75L')
                print('Seats-5')
                print('Price-22.60 Lakh')
                p=2260000

            if model_C == 5:
                c='NISSAN X TRAIL HYBRID'
                print('CC-1997')
                print('max power-147ps')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -150kmph')
                print('Mileage-11kmpl')
                print('Tank capacity-50l')
                print('Seats-5')
                print('Price-22.00 – 30.00 Lakh')
                p=3000000

            if model_C == 6:
                c='NISSAN SUNNY'
                print('CC-1498')
                print('BHP-99PS@6000rpm')
                print('Torque-134Nm@4000rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -160kmph')
                print('Mileage-16-20kmpl')
                print('Tank capacity-40Litres')
                print('Seats-5')
                print('Price-8.50 Lakh')
                p=850000

            if model_C == 7:
                c='NISSAN MICRA ACTIVE'
                print('CC-1198')
                print('BHP-67.04bhp@5000rpm')
                print('Torque-104Nm@4000rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -160kmph')
                print('Mileage-18.7kmpl')
                print('Tank capacity-40Litres')
                print('Seats-4')
                print('Price-3-4Lakhs')
                p=400000

            if model_C == 8:
                c='NISSAN MICRA'
                print('CC-1198')
                print('BHP-75.94bhp@6000rpm')
                print('Torque-104Nm@4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -130kmph')
                print('Mileage-19.34kmpl')
                print('Tank capacity-41Litres')
                print('Seats-5')
                print('Price-5.99 Lakh - 8.13 Lakh')
                p=813000

            if model_C == 9:
                c='NISSAN TERRANO'
                print('CC-1461 cc')
                print('BHP-85PS@3750rpm')
                print('Torque-200Nm@1900rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -140kmph')
                print('Mileage-17.1kmpl')
                print('Tank capacity-40Litres')
                print('Seats-5')
                print('Price-10Lakhs')
                p=1000000

            if model_C == 10:
                c='NISSAN PATROL'
                print('CC-5552')
                print('BHP-399.62 BHP @ 5800 rpm')
                print('Torque-  560 NM @ 4000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -140kmph')
                print('Mileage-14.4kmpl')
                print('Tank capacity-140Litres')
                print('Seats-7')
                print('Price-12Lakhs')
                p=1200000

            elif model_C < 1 or model_C > 10:
                print('Select the appropriate model ')
                cars()
        if a == 11:
            bb='PAGANI'
            print('[1]PAGANI Huayra ')
            print('[2]PAGANI Huayra BC')
            print('[3]PAGANI Huayra Roadster')
            print('[4]PAGANI Huayra Roadster BC ')
            print('[5]PAGANI Huayra La Monza ')
            print('[6]PAGANI Huayra Codalunga')
            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='PAGANI Huayra'
                print('CC-5980')
                print('BHP-700 Bhp')
                print('Torque-1000 Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -370kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-₹ 1500,00,000')
                p=150000000

            if model_C == 2:
                c='AGANI Huayra BC'
                print('CC-5980cc')
                print('BHP-791 hp @ 5,900 rpm (590 kW)')
                print('Torque-774 lb·ft @ 2,000 – 5,600 rpm (1,049 N·m)')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -383kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-120Litres')
                print('Seats-2')
                print('Price-30.9Crore')
                p=309000000

            if model_C == 3:
                c='PAGANI Huayra Roadster'
                print('CC-5980')
                print('BHP-740 PS (544 kW; 730 hp) at 5,800 rpm')
                print('Torque- 1,000 N⋅m (738 lbf⋅ft) of torque at 2,250-4,500 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -340kmph')
                print('Mileage-6kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-61-83Crore')
                p=618300000

            if model_C == 4:
                c='PAGANI Huayra Roadster BC'
                print('CC-5980')
                print('BHP-791 hp @ 5,900 rpm (590 kW)')
                print('Torque-774 lb·ft @ 2,000 – 5,600 rpm (1,049 N·m)')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -380kmph')
                print('Mileage-5kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-30.9Crore')
                p=309000000

            if model_C == 5:
                c='PAGANI Huayra La Monza'
                print('CC-5980')
                print('BHP-740 PS (544 kW; 730 hp) ')
                print('Torque-740Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -230 mph')
                print('Mileage-kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-30.9Crore')
                p=309000000

            if model_C == 6:
                c='AGANI Huayra Codalunga'
                print('CC-5980')
                print('BHP-840 CV (618 kW) at 5,900 rpm')
                print('Torque-1,100 Nm from 2,000 rpm to 5,600 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -380kmph')
                print('Mileage-4kmpl')
                print('Tank capacity-120Litres')
                print('Seats-2')
                print('Price-60Crore')
                p=600000000
            elif model_C < 1 or model_C > 10:
                print('Select the appropriate model ')
                cars()
        if a == 12:
            bb='PORSCHE'
            print('[1]PORSCHE CAYENNE')
            print('[2]PORSCHE MACAN')
            print('[3]PORSCHE 911')
            print('[4]PORSCHE 718')
            print('[5]PORSCHE PANAMERA')
            print('[6]PORSCHE TAYCAN')
            print('[7]PORSCHE CAYENNE COUPE')
            print('[8]PORSCHE CROSS TURISMO')

            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='PORSCHE CAYENNE'
                print('CC-3998')
                print('BHP-550bhp@5750-6000rpm')
                print('Torque-770Nm@1960-4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -210kmph')
                print('Mileage-7kmpl')
                print('Tank capacity-90Litres')
                print('Seats-5')
                print('Price-27 - 1.93 Cr')
                p=19300000

            if model_C == 2:
                c='PORSCHE MACAN'
                print('CC-2894')
                print('BHP-434.49bhp@5700-6600rpm')
                print('Torque-550Nm@1900-5600rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -230kmph')
                print('Mileage-11.24kmpl')
                print('Tank capacity-65Litres')
                print('Seats-5')
                print('Price-83.21 Lakh - 1.47 Cr')
                p=14700000

            if model_C == 3:
                c='PORSCHE 911'
                print('CC-3996')
                print('BHP-641.00bhp@6500')
                print('Torque-450Nm1950–5000')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -210kmph')
                print('Mileage-10kmpl')
                print('Tank capacity-64Litres')
                print('Seats-2,4')
                print('Price-1.73 - 3.14 Cr')
                p=31400000

            if model_C == 4:
                c='PORSCHE 718'
                print('CC-3997')
                print('BHP-493.49bhp@8400rpm')
                print('Torque-450Nm@6750rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-9.17kmpl')
                print('Tank capacity-64Litres')
                print('Seats-2')
                print('Price-1.37 - 2.54 Cr')
                p=25400000

            if model_C == 5:
                c='PORSCHE PANAMERA'
                print('CC-3996')
                print('BHP-680bhp@5750-6000rpm')
                print('Torque-770nm@1960-4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -220kmph')
                print('Mileage-10.75kmpl')
                print('Tank capacity-64Litres')
                print('Seats-4')
                print('Price-1.58 - 2.71 Cr')
                p=27100000

            if model_C == 6:
                c='PORSCHE TAYCAN'
                print('CC-3996')
                print('BHP-482.76bhp')
                print('Torque-650Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Range-388-452km')
                print('Seats-2')
                print('Price-1.53 - 2.34 Cr')
                p=23400000 

            if model_C == 7:
                c='PORSCHE CAYENNE COUPE'
                print('CC-3996')
                print('BHP-631.62bhp@6000rpm')
                print('Torque-850Nm@2300to4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED - 220kmph')
                print('Mileage-11kmpl')
                print('Seats-4')
                print('Price-1.35 - 2.57 Cr')
                p=25700000

            if model_C == 8:
                c='PORSCHE CROSS TURISMO'
                print('BHP-482.76bhp')
                print('Torque-650Nm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -240 to 250 kmph')
                print('range-388-452km')
                print('Tank capacity-60L')
                print('Seats-5')
                print('Price-1.74 Cr')
                p=17400000


            elif model_C < 1 or model_C > 10:
                print('Select the appropriate model ')
                cars()
        if a == 13:
            bb='ROLLS ROYCE'
            print('[1]ROLLS ROYCE PHANTOM ')
            print('[2]ROLLS ROYCE WRAITH')
            print('[3]ROLLS ROYCE CULLIAN')
            print('[4]ROLLS ROYCE DAWN')
            print('[5]ROLLS ROYCE GHOST')

            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='ROLLS ROYCE PHANTOM'
                print('CC-6749')
                print('BHP-563bhp@5000rpm')
                print('Torque-900Nm@1700rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -280kmph')
                print('Mileage-9.8kmpl')
                print('Tank capacity-100Litres')
                print('Seats-5')
                print('Price-8.99 - 10.48 Cr')
                p=104800000

            if model_C == 2:
                c='ROLLS ROYCE WRAITH'
                print('CC-6592cc')
                print('BHP-591bhp@5000-5500rpm')
                print('Torque-900Nm1700-4500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -290kmph')
                print('Mileage-10.2kmpl')
                print('Tank capacity-83Litres')
                print('Seats-4')
                print('Price-6.22 - 7.21 Cr')
                p=72100000

            if model_C == 3:
                c='ROLLS ROYCE CULLIAN'
                print('CC-6750')
                print('BHP-563bhp@5000rpm')
                print('Torque-850Nm@1600rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -280kmph')
                print('Mileage-9.5kmpl')
                print('Tank capacity-')
                print('Seats-5')
                print('Price-6.95 Cr')
                p=69500000

            if model_C == 4:
                c='ROLLS ROYCE DAWN'
                print('CC-6598')
                print('BHP-563bhp@5250-6000rpm')
                print('Torque-820Nm@1500-5000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -280kmph')
                print('Mileage-9.8 kmpl')
                print('Tank capacity-')
                print('Seats-4')
                print('Price-7.30 - 7.85 Cr')
                p=78500000

            if model_C == 5:
                c='ROLLS ROYCE GHOST'
                print('CC-6750')
                print('BHP-563bhp@5250rpm')
                print('Torque-820Nm@1500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -260kmph')
                print('Mileage-6.33kmpl')
                print('Tank capacity-')
                print('Seats-5')
                print('Price-6.95 - 7.95 Cr')
                p=79500000

            elif model_C < 1 or model_C > 6:
                print('Select the appropriate model ')
                cars()

        if a == 14:
            bb='TOYATA'
            print('[1]TOYATA URBAN CRUISER')
            print('[2]TOYOTA CAMRY')
            print('[3]TOYATA FORTUNER')
            print('[4]TOYATA VELLFIRE')
            print('[5]TOYATA INNOVA CRYSTA')
            print('[6]TOYATA GLANZA')
            print('[7]TOYATA LAND CRUISER')
            print('[8]TOYATA RUMION')
            print('[9]TOYATA SUPRA')

            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='TOYATA URBAN CRUISER'
                print('CC-1462')
                print('BHP-103.26bhp@6000rpm')
                print('Torque-138nm@4400rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -170+kmph')
                print('Mileage-18.76 kmpl')
                print('Tank capacity-48Litres')
                print('Seats-5')
                print('Price-9.03 - 11.73 Lakh')
                p=1173000

            if model_C == 2:
                c='TOYOTA CAMRY'
                print('CC-2487 cc')
                print('BHP-178 HP @ 5700 rpm')
                print('Torque-221 Nm @ 3600-5200 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -190kmph')
                print('Mileage-19.16 kmpl')
                print('Tank capacity-50Litres')
                print('Seats-5')
                print('Price-44.00-45.00Lakhs')
                p=4500000

            if model_C == 3:
                c='TOYATA FORTUNER'
                print('CC-2755')
                print('BHP-204 HP @ 3400 rpm')
                print('Torque-420 Nm @ 1400 - 3400 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -190+ kmph')
                print('Mileage-14.24 kmpl')
                print('Tank capacity-80Litres')
                print('Seats-7')
                print('Price-32,40,000 - ₹ 49,57,000')
                p=34957000

            if model_C == 4:
                c='TOYATA VELLFIRE'
                print('CC-2494')
                print('BHP-115 HP @ 4700 rpm')
                print('Torque-  198 Nm @ 2800-4000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -170 kmph')
                print('Mileage-16.35 kmpl')
                print('Tank capacity-58Litres')
                print('Seats-7')
                print('Price-92,60,000')
                p=9260000

            if model_C == 5:
                c='TOYATA INNOVA CRYSTA'
                print('CC-2393')
                print('BHP-150 HP @ 3400 rpm')
                print('Torque-343 Nm @ 1400-2800 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -175+kmph')
                print('Mileage-13.6kmpl')
                print('Tank capacity-55Litres')
                print('Seats-7')
                print('Price-17,86,000 - ₹ 26,54,000')
                p=2654000

            if model_C == 6:
                c='TOYATA GLANZA'
                print('CC-1197')
                print('BHP-89 HP @ 6000 rpm')
                print('Torque-113 Nm @ 4400 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -180kmph')
                print('Mileage- 22.35 kmpl')
                print('Tank capacity-37Litres')
                print('Seats-4')
                print('Price-6,59,000 - ₹ 9,98,900')
                p=998900

            if model_C == 7:
                c='TOYATA LAND CRUISER'
                print('CC-4461')
                print('BHP-563bhp@5250-6000rpm')
                print('Torque-820Nm@1500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -280kmph')
                print('Mileage-11.1kmpl')
                print('Tank capacity-110Litres')
                print('Seats-7')
                print('Price-1.50 Cr')
                p=15000000

            if model_C == 8:
                c='TOYATA RUMION'
                print('CC-1462')
                print('BHP-103.25bhp@6000rpm')
                print('Torque-138nm@4400rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -160kmph')
                print('Mileage-16kmpl')
                print('Tank capacity-40Litres')
                print('Seats-7')
                print('Price-8.77 Lakh')
                p=877000
            if model_C == 9:
                c='TOYATA SUPRA'
                print('CC-2998')
                print('BHP-563bhp@5250-6000rpm')
                print('Torque-820Nm@1500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -250kmph')
                print('Mileage-18kmpl')
                print('Tank capacity-60Litres')
                print('Seats-5')
                print('Price-3.5Crore')
                p=35000000

            elif model_C < 1 or model_C > 9:
                print('Select the appropriate model ')
                cars()
        if a == 15:
            bb='VOLKSWAGEN'
            print('[1]VOLKSWAGEN VIRTUS')
            print('[2]VOLKSWAGEN TAIGUN')
            print('[3]VOLKSWAGEN TIGUAN')
            print('[4]VOLKSWAGEN VENTO')
            print('[5]VOLKSWAGEN POLO')
            print('[6]VOLKSWAGEN POLO GT')
            print('[7]VOLKSWAGEN AMEO')
            print('[8]VOLKSWAGEN VENTO')
            print('[9]VOLKSWAGEN PASSAT')
            print('[10]VOLKSWAGEN GOLF')
            print('[11]VOLKSWAGEN T-CROSS')
            print('[12]VOLKSWAGEN T-ROC')
            model_C = int(input('Select the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='VOLKSWAGEN VIRTUS'
                print('CC-1498')
                print('BHP-147.51bhp@5000-6000rpm')
                print('Torque-250Nm@1600-3500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -150kmph')
                print('Mileage-18.67 kmpl')
                print('Tank capacity-45Litres')
                print('Seats-5')
                print('Price-11.22 - 17.92 Lakh')
                p=1792000

            if model_C == 2:
                c='VOLKSWAGEN TAIGUN'
                print('CC-1498')
                print('BHP-147.51bhp@5000-6000rpm')
                print('Torque-250nm@1600-3500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -180kmph')
                print('Mileage-13.64 kmpl')
                print('Tank capacity-50Litres')
                print('Seats-5')
                print('Price-11.40 - 18.60 Lakh')
                p=1860000

            if model_C == 3:
                c='VOLKSWAGEN TIGUAN'
                print('CC-1984')
                print('BHP-187.74bhp@4200-6000rpm')
                print('Torque-320Nm@1500-4100rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -160kmph')
                print('Mileage-12.65 kmpl')
                print('Tank capacity-60Litres')
                print('Seats-5')
                print('Price-32.79 Lakh')
                p=3279000

            if model_C == 4:
                c='VOLKSWAGEN VENTO'
                print('CC-999')
                print('BHP-108.62bhp@5000-5500rpm')
                print('Torque-175Nm@1750-4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -160kmph')
                print('Mileage-16.0kmpl')
                print('Tank capacity-55Litres')
                print('Seats-5')
                print('Price-10.00 - 14.44 Lakh')
                p=1444000

            if model_C == 5:
                c='VOLKSWAGEN POLO'
                print('CC-999')
                print('BHP-108.495bhp@4000rpm')
                print('Torque-250Nm@1500-3000rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -140kmph')
                print('Mileage-12.4kmpl')
                print('Tank capacity-65L')
                print('Seats-5')
                print('Price-8Lakh')
                p=800000

            if model_C == 6:
                c='VOLKSWAGEN POLO GT'
                print('CC-999 to 1498 cc')
                print('BHP-108.495bhp@4000rpm')
                print('Torque-250Nm@1500-3000rpmSeating')
                print('TRANSMISSION-Manual & Automatic')
                print('TOP SPEED -130kmph')
                print('Mileage-17.83 to 21.73 kmpl')
                print('Tank capacity-45Litres')
                print('Seats-5')
                print('Price-5.67 Lakh')
                p=567000

            if model_C == 7:
                c='VOLKSWAGEN AMEO'
                print('CC-999')
                print('BHP-108.62bhp@5000-5500rpm')
                print('Torque-175Nm@1750-4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -')
                print('Mileage-16.35kmpl')
                print('Tank capacity-55Litres')
                print('Seats-5')
                print('Price-10.00 - 14.44 Lakh')
                p=1444000

            if model_C == 8:
                c='VOLKSWAGEN VENTO'
                print('CC-999')
                print('BHP-108.62bhp@5000-5500rpm')
                print('Torque-175Nm@1750-4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -')
                print('Mileage-16.35 kmpl')
                print('Tank capacity-55Litres')
                print('Seats-5')
                print('Price-10.00 - 14.44 Lakh')
                p=1444000

            if model_C == 9:
                c='VOLKSWAGEN PASSAT'
                print('CC-999 to 1498 cc')
                print('BHP-108.495bhp@4000rpm')
                print('Torque-250Nm@1500-3000rpmSeating')
                print('TRANSMISSION-Manual & Automatic')
                print('TOP SPEED -130kmph')
                print('Mileage-17.83 to 21.73 kmpl')
                print('Tank capacity-45Litres')
                print('Seats-5')
                print('Price-5.67 Lakh')
                p=567000

            if model_C == 10:
                c='VOLKSWAGEN GOLF'
                print('CC-999')
                print('BHP-108.62bhp@5000-5500rpm')
                print('Torque-175Nm@1750-4000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -')
                print('Mileage-16.35 kmpl')
                print('Tank capacity-55Litres')
                print('Seats-5')
                print('Price-10.00 - 14.44 Lakh')
                p=1444000

            if model_C == 11:
                c='VOLKSWAGEN T-CROSS'
                print('CC-1498')
                print('BHP-147.51bhp@5000-6000rpm')
                print('Torque-250nm@1600-3500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -180kmph')
                print('Mileage-13.64 kmpl')
                print('Tank capacity-50Litres')
                print('Seats-5')
                print('Price-11.40 - 18.60 Lakh')
                p=1860000

            if model_C == 12:
                c='VOLKSWAGEN T-ROC'
                print('CC-999')
                print('BHP-108.495bhp@4000rpm')
                print('Torque-250Nm@1500-3000rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -140kmph')
                print('Mileage-12.4kmpl')
                print('Tank capacity-65L')
                print('Seats-5')
                print('Price-8Lakh')
                p=800000
            elif model_C < 1 or model_C > 12:
                print('Select the appropriate model ')
                cars()
        if a == 16:
            bb='Aston Martin'
            print('[1]ASTON MARTIN DBC1')
            print('[2]ASTON MARTIN DBX')
            print('[3]ASTON MARTIN VANTAGE')
            print('[4]ASTON MARTIN VANTAGE ROADSTER')
            print('[5]ASTON MARTIN VANTAGE F1 EDITION')
            print('[6]ASTON MARTIN DBS SUPERLEGGER')
            print('[7]ASTON MARTIN VANTAGE V12')
            print('[8]ASTON MARTIN VANTAGE V8')
            print('[9]ASTON MARTIN VANTAGE V8 VOLANBE')
            print('[10]ASTON MARTIN VALKYRIE')
            print('[11]ASTON MARTIN SPEEDSTER')
            print('[12]ASTON MARTIN VALHALLA')
            print('[13]ASTON MARTIN DBS')
            model_C = int(input('Enter the Model:'))
            print('\nSPECIFICATIONS')
            if model_C == 1:
                c='ASTON MARTIN DBC1'
                print('CC-5198')
                print('BHP-608PS@6500rpm')
                print('Torque-700Nm@1500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -335 kmph')
                print('Mileage-6kmpl')
                print('Tank capacity-50L')
                print('Seats-2')
                print('Price-4Crores')
                p=40000000

            if model_C == 2:
                c='ASTON MARTIN DBX'
                print('CC-3982')
                print('BHP-542bhp@6500rpm')
                print('Torque-700Nm@2200-5000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -')
                print('Mileage-6.99 kmpl')
                print('Tank capacity-85l')
                print('Seats-5')
                print('Price-3.82 Cr')
                p=38200000

            if model_C == 3:
                c='ASTON MARTIN VANTAGE'
                print('CC-3998')
                print('BHP-502.88Bhp@6000rpm')
                print('Torque-675Nm@2000-5000rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -')
                print('Mileage-7.49kmpl')
                print('Tank capacity-73')
                print('Seats-2')
                print('Price-3.00 - 3.50 Cr')
                p=35000000

            if model_C == 4:
                c='ASTON MARTIN VANTAGE ROADSTER'
                print('CC-3998')
                print('BHP-502.88Bhp@6000rpm')
                print('Torque-@2000-5000rpm')
                print('TRANSMISSION-Manual')
                print('TOP SPEED -')
                print('Mileage-7.46 kmpl')
                print('Tank capacity-73Litres')
                print('Seats-2')
                print('Price-3.50Crore')
                p=35000000

            if model_C == 5:
                c='ASTON MARTIN VANTAGE F1 EDITION'
                print('CC-3999')
                print('BHP-527@rpm')
                print('Torque-623@rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -312 kmph')
                print('Mileage-6 kmpl')
                print('Tank capacity-80Litres')
                print('Seats-4')
                print('Price-1.21Crore')
                p=12100000

            if model_C == 6:
                c='ASTON MARTIN DBS SUPERLEGGER'
                print('CC-5204')
                print('BHP-715 bhp @ 6500 rpm')
                print('Torque-900Nm @ 5700 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -345 kmph')
                print('Mileage-7.1kmpl')
                print('Tank capacity-100Litres')
                print('Seats-2')
                print('Price-5Crore')
                p=50000000

            if model_C == 7:
                c='ASTON MARTIN VANTAGE V12'
                print('CC-5935')
                print('BHP-380 bhp @ 6500 rpm')
                print('Torque-570 Nm @ 5750 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -320 kmph')
                print('Mileage-11kmpl')
                print('Tank capacity-50Litres')
                print('Seats-2')
                print('Price-3.60 Crore')
                p=36000000

            if model_C == 8:
                c='ASTON MARTIN VANTAGE V8'
                print('CC-3982')
                print('BHP-503 bhp @ 6000 rpm')
                print('Torque-685 Nm @ 2000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -314 kmph')
                print('Mileage-8.6kmpl')
                print('Tank capacity-50Litres')
                print('Seats-2')
                print('Price-2.95 Crore')
                p=29500000

            if model_C == 9:
                c='ASTON MARTIN VANTAGE V8 VOLANBE'
                print('CC-3982')
                print('BHP-370 HP / 375 PS / 276 kW @ 6000 rpm')
                print('Torque-685 Nm @ 2000-5000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -314kmph')
                print('Mileage-9.4kmpl')
                print('Tank capacity-60L')
                print('Seats-5')
                print('Price-3 Crores')
                p=30000000

            if model_C == 10:
                c='ASTON MARTIN VALKYRIE'
                print('CC-6500')
                print('BHP-1160bhp@10500rpm')
                print('Torque-740Nm of torque at 7,000rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -310kmph')
                print('Mileage-8.2kmpl')
                print('Tank capacity-85Litres')
                print('Seats-5')
                print('Price-3.40Crore')
                p=34000000

            if model_C == 11:
                c='ASTON MARTIN SPEEDSTER'
                print('CC-5935')
                print('BHP-380 bhp @ 6500 rpm')
                print('Torque-570 Nm @ 5750 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -300 kmph')
                print('Mileage-11kmpl')
                print('Tank capacity-50Litres')
                print('Seats-2')
                print('Price-3.60 Crore')
                p=36000000

            if model_C == 12:
                c='ASTON MARTIN VALHALLA'
                print('CC-3982')
                print('BHP-503 bhp @ 6000 rpm')
                print('Torque-685 Nm @ 2000 rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -347 kmph')
                print('Mileage-8.6kmpl')
                print('Tank capacity-50Litres')
                print('Seats-2')
                print('Price-2.95 Crore')
                p=29500000

            if model_C == 13:
                c='ASTON MARTIN DBS'
                print('CC-5198')
                print('BHP-608PS@6500rpm')
                print('Torque-700Nm@1500rpm')
                print('TRANSMISSION-Automatic')
                print('TOP SPEED -337 kmph')
                print('Mileage-6kmpl')
                print('Tank capacity-50l')
                print('Seats-2')
                print('Price-4Crores')
                p=40000000
            elif model_C < 1 or model_C > 13:
                print('Select the appropriate model ')
                cars()
        elif a < 1 or a > 16:
            print('Select the appropriate brand ')
            incars()
    incars()
    def cont():
        while True:
            print('\n\t\t\tPress 1 to confirm your booking \n\t\t\tPress 2 to select again\n\t\t\tPress 3 to quit')
            w=input('Enter your choice :')           
            if w=='1':  
              while True:
                  global n
                  n=input('Enter username:')
                  f=open('login.csv','r',newline="")
                  l=[]
                  a=csv.reader(f)
                  for i in a:
                      if len(i)>2:
                           l.append(i[0])
                  if n not in l:
                    print('Enter valid username')
                    continue
                  else:
                      break
                  f.close()
              while True:
                  e=input('Enter email: ')
                  if '@gmail.com' not in e :
                      print("Invalid mail id\nEnter again")
                      continue
                  else:
                      break                   
              x=random.randrange(10000,99999)
              while True:
                    ph=int(input('Enter mobile number :'))
                    if len(str(ph))>10 or len(str(ph))<10:
                        print('Enter valid number')
                        continue
                    else:
                        break
              amp=p*(0.3)
              status='pending'
              country=input('Enter Country/region:')
              pincode=input('Enter pincode:')
              city=input('Enter your city:')
              landmark=input('Enter landmark:')
              doorno=input('Enter your doorno:')
              book=open('car_booking.csv','a+')
              dob=date.today()
              td=datetime.timedelta(days=30)
              global dod
              dod=dob+td
              dob=str(dob)
              wr=csv.writer(book)
              t=[n,e,x,bb,c,p,amp,ph,status,country,pincode,city,landmark,doorno,dob,dod]
              wr.writerow(t)
              book.close()
              payment()               
            elif w=='2':
                cars()
                return True
            elif w=='3':
                print('Thank you visit again')
                return True
            else:
                print('ENTER A VALID CHOICE')
                continue
            break
    cont()
def user_edit():
    e=open("login.csv",'r+',newline="")
    yt=open('car_booking.csv','r+',newline="")
    wr=csv.reader(e)
    wo=csv.writer(e)
    wr1=csv.reader(yt)
    w01=csv.writer(yt)
    lll,lll1=[],[]
    a,a1=[],[]
    b,b1=[],[]
    user=input("Enter username:")
    mail=input("Enter email id:")
    passwd=input("Enter password:")
    lst=[user,mail,passwd]
    for i in wr:
        lll.append(i)
    for w in wr1:
        lll1.append(w)
    if lst in lll:
        for j in lll :
            a.append(j[0])
            b.append(j[1])
            if user in a and mail in b:
                print("1)USERNAME")
                print("2)EMAIL ID")
                print("3)PASSWORD")
                print("4)Address")                
                detail=input("Enter detail you would like to change:")
                if detail=='1':
                    newname=input("Enter new user name:")
                    j[0]=newname
                    dd=[]
                    with open("login.csv",'w',newline="") as q:
                        x=csv.writer(q)
                        x.writerows(lll)
                        print("Success")
                        
                    with open('car_booking.csv','a+',newline="") as Q:
                        fg=csv.writer(Q)
                        fgr=csv.reader(Q)
                        for i in Q:
                            i.append(dd)
                        for j in range(len(dd)):
                            if dd[j][0]==user:
                                dd[j][0]=newname
                            else:
                                continue
                        fg.writerows(dd)
                        return True
                    
                elif detail=='2':
                    newmail=input("Enter new user mail id:")
                    j[1]=newmail
                    dx=[]
                    with open("login.csv",'w',newline="") as q:
                        x=csv.writer(q)
                        x.writerows(lll)
                        print("Success")
                    with open('car_booking.csv','a+') as Q:
                        rr=csv.writer(Q)
                        rr1=csv.reader(Q)
                        for i in Q:
                            i.append(dx)
                        for j in range(len(dx)):
                            if dx[j][1]==name:
                                dx[j][1]=newmail
                            else:
                                continue
                        rr.writerows(dx)
                        return True                    
                elif detail=='3':
                    while True:
                        newpass=input("Enter new password:")
                        npass=input("Re enter password:")
                        if newpass==npass:
                            j[2]=npass
                            with open("login.csv",'w',newline="") as q:
                                x=csv.writer(q)
                                x.writerows(lll)
                                print("Success")
                                return True
                        else:
                            print("Enter correct password again")
                            continue

                elif detail == '4':
                        print('\nENTER NEW DETAILS')
                        pincode=input('Enter pincode:')
                        city=input('Enter city:')
                        landmark=input('Enter landmark:')
                        doorno=input('Enter your doorno:')
                        ed=[]
                        with open('car_booking.csv','r') as F:
                            re=csv.reader(F)
                            wr=csv.writer(F)
                            for i in re:
                                if len(i)>5:
                                    ed.append(i)
                                else:
                                    continue
                            
                        for j in range(len(ed)):
                            if ed[j][0] == user:
                                ed[j][10]=pincode
                                ed[j][11]=city
                                ed[j][12]=landmark
                                ed[j][13]=doorno
                            else:
                                continue
                        
                        with open('car_booking.csv','w',newline='\n')as GG:
                            wr=csv.writer(GG)
                            wr.writerows(ed)
                print('Success')
     
                                                        
        
def register():
    f=open('login.csv','a+',newline="")
    wo1=csv.writer(f,delimiter=',')   
    while True:
        f=open('login.csv','r+',newline="")
        username=input("Enter username  :")
        l=[]
        a=csv.reader(f)
        for i in a:
            if len(i) >2:
                l.append(i[0])
        if username in l:
            print("User name already taken")
            continue
        else:
            break
        f.close()
    
    #email
    while True:
        f=open('login.csv','r',newline="")
        a=csv.reader(f)
        l2=[]
        usermail=input("Enter email id    :")
        if '@gmail.com' not in usermail :
            print("Invalid mail id\nEnter again")
            continue
        
        else:
            for i in a :
                if len(i)>2:
                    l2.append(i[1])
            if usermail in l2:
                print("Account already exists with this mail id")
                continue
            else:
                break
        f.close()
        break


    #password
    while True:
        password=input("Enter password:")
        password2=input("Re-enter password:")
        if password!=password2:
            print("Password do not match match")
            print("Enter again")
            continue
        else:
            print("Password match")
            print("Registeration successful!")
            print("Welcome", username)
            break   
    wo1.writerow([username,usermail,password])
    f.close()
    return 'success'

def login():
    while True:
        b = []
        name = input("Enter your username:")
        print()
        email = input('Enter your email:')
        print()
        password = input('Enter your password:')
        print()
        with open('login.csv', 'r+', newline='\r\n') as f:
            reader = csv.reader(f)
            for row in reader:
                b.append(row)
        lst = [name, email, password]
                
        if lst in b:
            print("Login successful")
            print()
            print("Welcome", name)
            et=[]
            with open('car_booking.csv','r+')as f:
                reader=csv.reader(f)
                for i in reader:
                    if len(i)>2:
                        et.append(i[0])
            if name in et:
                print('*'*108)
                while True:
                    print('\t\t\t\t|-----------------------------|')
                    print('\t\t\t\t|1.  TO VIEW PERSONAL DETAILS |')
                    print('\t\t\t\t|2.  TO EDIT PERSONAL DETAILS |')
                    print("\t\t\t\t|3.  TO CANCEL YOUR BOOKING   |")
                    print("\t\t\t\t|4.  LOG OUT                  |")
                    print('\t\t\t\t|-----------------------------|')
                    print('*'*117)
                    hh=input('Enter your choice:')
                    if hh=='1':
                        ep=[]
                        with open('car_booking.csv','r') as G:    
                            r=csv.reader(G)
                            for i in r:
                                if len(i)>=5:
                                    ep.append(i)
                            perd=[]
                            ra=['NAME :','GMAIL :','ID :','BRAND :','MODEL :','TOTAL AMOUNT :','AMOUNT PAID :','PHONE NO. :','COUNTRY :','PINCODE :','CITY :','LANDMARK :','DOORNO :','DATE OF BOOKING :','EXPECTED DATE OF ARRIVAL :']
                            for j in range(len(ep)):
                                if ep[j][0] == name:
                                    #print(ep[j])
                                    perd=ep[j]
                                    #perd.append(ep[j])
                            perd.remove('Paid')                            
                            for k in range(len(ra)):
                                for l in range(len(perd)):
                                    if k==l:
                                        print(ra[k],perd[l])                                                                                                                               
                    elif hh=='2': 
                        user_edit()
                    
                    elif hh=='3':
                        df=[]
                        tday=datetime.date.today()
                        with open('car_booking.csv','r') as J:
                            dg=csv.reader(J)
                            for i in dg:
                                if len(i)>5:
                                    df.append(i)
                                else:
                                    continue
                            for k in range(len(df)):
                                if df[k][0]== name:
                                    dat=df[k][-1]
                                    datx=datetime.datetime.strptime(dat, '%d-%m-%Y').date()
                                    remdays=datx-tday
                                    remdays=str(remdays)
                                    remdays_str=remdays[0:2]
                                    remdays_int=int(remdays_str)
                        if remdays_int <= 10:
                            print('You cannot cancel your booking now!!')
                        if remdays_int > 10:
                            global can
                            xg,ep,can=[],[],[]
                            with open('car_booking.csv','r') as G:    
                                r=csv.reader(G)
                                for i in r:
                                    if len(i)>=5:
                                        ep.append(i)
                            with open('car_booking.csv','w') as H:
                                    for j in range(len(ep)):
                                        wr=csv.writer(H)
                                        if ep[j][0]==name:
                                            can.append(ep[j])
                                            with open('cancelled_booking.csv','a+',newline='') as CC:
                                                ds=csv.writer(CC)
                                                ds.writerows(can)
                                        else:
                                            if len(ep[j])>5:
                                                xg.append(ep[j])
                                    wr.writerows(xg)
                                    print('The amount will be transferred to your account within 7 working days\nThank you')
                            break
                    elif hh=='4':
                        break
            else:
                cars()
                                                                               
        elif lst not in b:
            print("Wrong credentials!")
            print()
            x = input("Would you like to enter details again (or) create new account?(a/c):")
            print()
            if x == 'c':
                register()
            elif x == 'a':
                continue
            else:
                print("Enter valid choice:")
                continue

        f.close()
        break


def payment():
    while True:
        ll,l,d,c=[],[],[],[]
        #c--> amount
        #d--> [[name,amount]]
        #l--> [name]       
        with open('car_booking.csv','r',newline='') as f:
            g1=[]
            a=csv.reader(f)                
            for i in a:
                if len(i)>2:
                    if i[8]=='pending':
                        g1=[i[0],i[6]]
                        l.append(i[0])
                        c.append(i[6])
                        d.append(i)
                    else:
                        continue
                    
        n=input('Enter your name:')
        if n in l :
            print("Modes of payment")
            print("1.upi")
            print("2.card")
            x=input("Enter mode of payment:")
            if x == "1":
                y = ""
                print("Select the upi domain")
                print("1.@apl")
                print("2.@yapl")
                print("3.axisb")
                print("4.idfcbank")
                print("5.@icici")
                print("6.@axisbank")
                print("7.@okaxis")
                print("8.@okhdfcbank")
                print("9.@okicici")
                print("10.@oksbi")
                upi = int(input("Enter the required upi domain:"))
                if upi == 1:
                    y += "@apl"
                elif upi == 2:
                    y += "@yapl"
                elif upi == 3:
                    y += "@axixb"
                elif upi == 4:
                    y += "@idfcbank"
                elif upi == 5:
                    y += "@icici"
                elif upi == 6:
                    y += "@axisbank"
                elif upi == 7:
                    y += "@okaxis"
                elif upi == 8:
                    y += "@okkhdfcbank"
                elif upi == 9:
                    y += "@okicici"
                elif upi == 10:
                    y += "@oksbi"
                else:
                    print("Improper domain please try again")
                while True:
                    user = input("Enter your upi id:")
                    if len(user)>8:
                        print("Invalid user id")
                        continue
                    elif len(user)>5 or len(user)<=8:
                        break
                user = user.join(y)
                for i in d:
                    if n in i:
                        while True:
                            s=float(i[6])
                            print("Cost:",i[6])
                            x=float(input("Enter the amount to be transferred:"))
                            if x==s:
                                print()
                                break
                            else:
                                print('Please retry again')
                                continue
                            
                while True:
                    pin = int(input("Enter your upi pin:"))
                    if len(str(pin))!=4:
                        print("Enter valid pin")
                        continue
                    else:
                        print("Transfer sucessful")
                        e=open('car_booking.csv','r+')
                        b=csv.reader(e)
                        for i in b:
                            ll.append(i)
                        for j in ll:
                            if n in j:
                                j[8]='Paid'
                                with open('car_booking.csv','w',newline="") as f:
                                    x=csv.writer(f)
                                    x.writerows(ll)
                        print('RECIEPT')
                        ggg=str(x)
                        zh=datetime.datetime.now()
                        ddd=zh.date()
                        t=zh.time()
                        ddd=str(ddd)
                        t=str(t)
                        for k in ll:
                            if n in k:  
                                billno=random.randrange(10000000,99999999)                                    
                                print('\t\t\t|-----------------------------------------------------------------------|')
                                print('\t\t\t|                                                                       |')
                                print('\t\t\t|  *******************************************************************  |')
                                print('\t\t\t|  *                            RECIEPT                              *  |')
                                print('\t\t\t|  *******************************************************************  |')
                                print('\t\t\t|  *                               DATE :{:10}'.format(ddd),'                 *  |')
                                print('\t\t\t|  *  BILLNO:',billno, '                                              *  |')
                                print('\t\t\t|  *                               TIME :{:15}'.format(t),'            *  |')
                                print('\t\t\t|  *******************************************************************  |')
                                print('\t\t\t|  *                                                                 *  |')
                                print('\t\t\t|  *            Sender            :{:20}'.format(n),'             *  |')
                                print('\t\t\t|  *                                                                 *  |')
                                print('\t\t\t|  *            Reciever          :EMIRATES                          *  |')
                                print('\t\t\t|  *                                                                 *  |')
                                print('\t\t\t|  *            Car booking cost  :{:9}'.format(k[6]),'                        *  |')
                                print('\t\t\t|  *                                                                 *  |')
                                print('\t\t\t|  *            Amount Paid       :{:9}'.format(k[6]),'                        *  |')
                                print('\t\t\t|  *                                                                 *  |')
                                print('\t\t\t|  *                                                                 *  |')
                                print('\t\t\t|  *******************************************************************  |')
                                print('\t\t\t|  *-----------------THANK YOU FOR USING OUR SERVICE-----------------*  |')
                                print('\t\t\t|  *******************************************************************  |')
                                print('\t\t\t|-----------------------------------------------------------------------|')
                                print('\n\n')
                                print('EXPECTED DATE OF ARRAIVAL :',dod)
                                print('THANK YOU FOR PURCHASING')
                                print()
                                uc=input('Do you want to surf again(1) or quit(2):')
                                print('Enter your choice (1 or 2)')
                                if uc=='1':
                                    break
                                if uc=='2':
                                    print('VISIT AGAIN')
                                    sys.exit()
                        return True
            elif x == "2":
                print("Select they type of card")
                print("1.Credit card")
                print("2.Debit card")
                card = int(input("Enter the type of card:"))
                if card == 1:
                    print("You have choosen for credit card")
                    print("Choose the credit card processor")
                    print("1.Mastercard")
                    print("2.Visa")
                    processor = int(input("Enter the processor type:"))
                    if processor == 1:
                        print("You have choosen for mastercard")
                        while True:
                            num = int(input("Enter the 16 digit card number:"))
                            num=str(num)
                            if len(num) == 16:
                                c = int(input("Enter the 3 digit cvv present at the back of the card:"))
                                c = str(c)
                                if len(c) == 3:
                                    while True:
                                        OTP=random.randrange(100000,999999)
                                        print("Your OTP is:",OTP)
                                        o = int(input("Enter the OTP sent:"))
                                        if o!=OTP:
                                            print("Enter the correct OTP")
                                            continue
                                        else:
                                            for i in d:
                                                if n in i:
                                                    while True:
                                                        s=float(i[6])
                                                        print("Cost:",i[6])
                                                        x=float(input("Enter the amount to be transferred:"))
                                                        if x>s:
                                                            print("Amount to be transferred is greater than the required amount")
                                                            continue
                                                        elif x<s:
                                                            print("Amount to be transferred is lesser then the required amount")
                                                            continue
                                                        else:
                                                            print("Transfer successful")
                                                            print()                                                        
                                                            e=open('car_booking.csv','r')
                                                            b=csv.reader(e)
                                                            for i in b:
                                                                ll.append(i)
                                                            for j in ll:
                                                                if n in j:
                                                                    j[8]='Paid'
                                                                    with open('car_booking.csv','w',newline="") as f:
                                                                        x=csv.writer(f)
                                                                        x.writerows(ll)
                                                            uc=input('Do you want to surf again(1) or quit(2):')
                                                            print('Enter your choice (1 or 2)')
                                                            if uc=='1':
                                                                break
                                                            if uc=='2':
                                                                print('VISIT AGAIN')
                                                                sys.exit()

                                                            break
                                            break
                            
                                else:
                                    print("Invalid cvv")
                                    continue
                            else:
                                print("Invalid card number")
                                continue
                            return True
                    elif processor == 2:
                            num = int(input("Enter the 16 digit card number:"))
                            num=str(num)
                            if len(num) == 16:
                                c = int(input("Enter the 3 digit cvv present at the back of the card:"))
                                c = str(c)
                                if len(c) == 3:
                                    while True:
                                        OTP=random.randrange(100000,999999)
                                        print("Your OTP is:",OTP)
                                        o = int(input("Enter the OTP :"))
                                        if o!=OTP:
                                            print("Enter the correct OTP")
                                            continue
                                        else:
                                            for i in d:
                                                if n in i:
                                                    while True:
                                                        s=float(i[6])
                                                        print("Cost:",i[6])
                                                        x=float(input("Enter the amount to be transferred:"))
                                                        if x>s:
                                                            print("Amount to be transferred is greater than the required amount")
                                                            continue
                                                        elif x<s:
                                                            print("Amount to be transferred is lesser then the required amount")
                                                            continue
                                                        else:
                                                            print("Transfer successful")
                                                            print()
                                                            e=open('car_booking.csv','r')
                                                            b=csv.reader(e)
                                                            for i in b:
                                                                ll.append(i)
                                                            for j in ll:
                                                                if n in j:
                                                                    j[8]='Paid'
                                                                    with open('car_booking.csv','w',newline="") as f:
                                                                        x=csv.writer(f)
                                                                        x.writerows(ll)
                                                            uc=input('Do you want to surf again(1) or quit(2):')
                                                            print('Enter your choice (1 or 2)')
                                                            if uc=='1':
                                                                break
                                                            if uc=='2':
                                                                print('VISIT AGAIN')
                                                                sys.exit()
                                                            break
                                            break                                    
                                else:
                                    print("Invalid cvv")
                                    continue
                            else:
                                print("Invalid card number")
                                continue
                            return True
                elif card == 2:
                    print("You have choosen for debit card")
                    print("Choose the credit card processor")
                    print("1.Mastercard")
                    print("2.Visa")
                    processor = int(input("Enter the processor type:"))
                    if processor == 1:
                            num = int(input("Enter the 16 digit card number:"))
                            num=str(num)
                            if len(num) == 16:
                                c = int(input("Enter the 3 digit cvv present at the back of the card:"))
                                c = str(c)
                                if len(c) == 3:
                                    while True:
                                        OTP=random.randrange(100000,999999)
                                        print("Your OTP is:",OTP)
                                        o = int(input("Enter the OTP :"))
                                        if o!=OTP:
                                            print("Enter the correct OTP")
                                            continue
                                        else:
                                            for i in d:
                                                if n in i:
                                                    while True:
                                                        s=float(i[6])
                                                        print("Cost:",i[6])
                                                        x=float(input("Enter the amount to be transferred:"))
                                                        if x>s:
                                                            print("Amount to be transferred is greater than the required amount")
                                                            continue
                                                        elif x<s:
                                                            print("Amount to be transferred is lesser then the required amount")
                                                            continue
                                                        else:
                                                            print("Transfer successful")
                                                            print()
                                                            e=open('car_booking.csv','r')
                                                            b=csv.reader(e)
                                                            for i in b:
                                                                ll.append(i)
                                                            for j in ll:
                                                                if n in j:
                                                                    j[8]='Paid'
                                                                    with open('car_booking.csv','w',newline="") as f:
                                                                        x=csv.writer(f)
                                                                        x.writerows(ll)
                                                            uc=input('Do you want to surf again(1) or quit(2):')
                                                            print('Enter your choice (1 or 2)')
                                                            if uc=='1':
                                                                break
                                                            if uc=='2':
                                                                print('VISIT AGAIN')
                                                                sys.exit()
                                                            break
                                            break              
                                else:
                                    print("Invalid cvv")
                                    continue
                            else:
                                print("Invalid card number")
                                continue
                            return True

                    elif processor == 2:
                        print("You have choosen for visa")
                        num = int(input("Enter the 16 digit card number:"))
                        num=str(num)
                        if len(num) == 16:
                            c = int(input("Enter the 3 digit cvv present at the back of the card:"))
                            c = str(c)
                            if len(c) == 3:
                                while True:
                                    OTP=random.randrange(100000,999999)
                                    print("Your OTP is:",OTP)
                                    o = int(input("Enter the OTP:"))
                                    if o!=OTP:
                                        print("Enter the correct OTP")
                                        continue
                                    else:
                                        for i in d:
                                            if n in i:
                                                while True:
                                                    s=float(i[1])
                                                    print("Cost:",i[1])
                                                    x=float(input("Enter the amount to be transferred:"))
                                                    if x>s:
                                                        print("Amount to be transferred is greater than the required amount")
                                                        continue
                                                    elif x<s:
                                                        print("Amount to be transferred is lesser then the required amount")
                                                        continue
                                                    else:
                                                        print("Transfer succssful")
                                                        print()
                                                        e=open('car_booking.csv','r')
                                                        b=csv.reader(e)
                                                        for i in b:
                                                            ll.append(i)
                                                        for j in ll:
                                                            if n in j:
                                                                j[8]='Paid'
                                                                with open('car_booking.csv','w',newline="") as f:
                                                                    x=csv.writer(f)
                                                                    x.writerows(ll)
                                                        uc=input('Do you want to surf again(1) or quit(2):')
                                                        print('Enter your choice (1 or 2)')
                                                        if uc=='1':
                                                            break
                                                        if uc=='2':
                                                            print('VISIT AGAIN')
                                                            sys.exit()
                                                        break
                                        break
                                
                                
                            else:
                                print("Invalid cvv")
                                continue
                        else:
                            print("Invalid card number")
                            continue
                        return True                       
        else:
            continue
       
def admin_login():
    al=[]
    io=0
    while True:
        a_id=input('Enter your admin id:')
        pwd=input('Enter your password:')
        with open('admin.csv','r') as af:
            ar=csv.reader(af)
            for i in ar:
                al.append(i)            
            for j in range(len(al)):
                if al[j][0]==a_id and al[j][2]==pwd:
                    print()
                    print('Welcome',al[j][1])
                    admin_choice()
                    break
            else:
                print('WRONG CREDENTIALS')
                print('Enter again\n')                
                io+=1
                if io<3:
                    continue
                else:
                    print('Suspicious login attempt')
                    sys.exit()
        break
                    
                
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
        for row in table:
            k+=1
            a=str(k)
            if len(a)==1:
                a='0'+a
                print('-'*(sum(l)+7))
            else:
                print('-'*(sum(l)+7))
            print(a+'|',r.format(*row))
        print('-'*(sum(l)+7))
    show(table)

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
            #userview('car_booking.csv')
            with open('car_booking.csv') as B:                
                red=csv.DictReader(B)
                cdd=[]      
                for i in red:
                    print(json.dumps(dict(i),indent=4))
                    print()
            continue
        if y == '3':
            #userview('cancelled_booking.csv')
            with open('cancelled_booking.csv') as B:                
                red=csv.DictReader(B)
                cdd=[]
                for i in red:
                    print(json.dumps(dict(i),indent=4))
                    print()

            
        if y== '4':
            print('LOGGED OUT SUCCESSFULLY')
            break            
        else:
            continue
                
      
def start():
    while True:
        print('''
                ##        ##   ##########  ##             #########        #####        ##        ##    ##########          
                ##        ##   ##          ##           ##               ##     ##      ## ##  ## ##    ##
                ##        ##   ##          ##          ##               ##       ##     ##   ##   ##    ##
                ##        ##   #######     ##         ##               ##         ##    ##        ##    #######
                ##   ##   ##   ##          ##          ##               ##       ##     ##        ##    ##
                ## ##  ## ##   ##          ##           ##               ##     ##      ##        ##    ##
                ##        ##   ##########  #########      #########        #####        ##        ##    ########## 

''')
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print('\t\t\t\t\t   |-------------------------------|')
        print("\t\t\t\t\t   |            EMIRATES           |")
        print("\t\t\t\t\t   |-------------------------------|")
        print('\t\t\t\t\t   |-------------------------------|')
        print('\t\t\t\t\t   |           MAIN MENU           |')
        print('\t\t\t\t\t   |-------------------------------|')
        print("\t\t\t\t\t   |           1.ADMIN             |")
        print("\t\t\t\t\t   |           2.USER              |")
        print("\t\t\t\t\t   |           3.EXIT              |")
        print('\t\t\t\t\t   |-------------------------------|')        
        print('--------------------------------------------------------------------------------------------------------------------------------')
        print("Select Your Option")
        print()
        u=int(input('Enter your choice:'))
        if u==1:
            admin_login()
        if u==2:
            while True:
                print('\t\t\t\t\t   |-------------------------------|')
                print('\t\t\t\t\t   |           MAIN MENU           |')
                print('\t\t\t\t\t   |-------------------------------|')
                print("\t\t\t\t\t   |           1.LOGIN             |")
                print("\t\t\t\t\t   |           2.REGISTER          |")
                print("\t\t\t\t\t   |           3.MAIN MENU         |")
                print('\t\t\t\t\t   |-------------------------------|')
                print('')
                print("Select Your Option")
                print()
                ch = input("Enter the choice:")
                print()
                if ch == '1':
                    login()
                    break
                elif ch == '2':                
                    s=register()
                    if s=='success':
                        cars()
                        break
                elif ch=='3':
                    break
                else:
                    print('Enter vaild choice')
                    continue
        if u==3:
            print('THANK YOU, VISIT AGAIN')
            sys.exit()
        else:
            continue
           
start()
              







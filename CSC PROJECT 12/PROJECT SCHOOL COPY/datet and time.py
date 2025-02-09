import datetime
''' #working with datetime.date
d=datetime.date(2000,10,11)
print(d)

tday=datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)#give the date
print(tday.weekday())
print(tday.isoweekday())

'''
'''
for isoweekday()  MONDAY 1  SUNDAY 7
for weekday() MONDAY 0  SUNDAY 6'''
'''
tdelta=datetime.timedelta(days=30)
print(tday+tdelta)

# date2=date1 + timedelta
# timedelta = date1+date2
print('\n\n')
bday=datetime.date(2023,6,29)
till_bday=bday-tday
print(till_bday)
print(till_bday.days)#prints only days
print(till_bday.total_seconds()) # prints total seconds

'''

# working with datetime.time

'''t=datetime.time(9,30,45,100000) # hours, min, sec, millsec
print(t)


bday=datetime.datetime(2023,6,29,00,00,00)
time_now=datetime.datetime.now()

tillbday=bday-time_now
print(tillbday)

tday=datetime.date.today()
print(tday)
'''
d='13-11-2022'
td=datetime.datetime.strptime(d, '%d-%m-%Y').date()
tday=datetime.date.today()
print(td)
print(tday)
tdel=td-tday
print(tdel)
tdel=str(tdel)
f=tdel[0:2]

print(f)
print(type(tdel))

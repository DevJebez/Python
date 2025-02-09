age=int(input())
year_of_passing=int(input())
annual_income=int(input())
arrear=int(input())
marks=float(input())
attendance=float(input())
imarks=int(marks)
iattendance=int(attendance)
if year_of_passing>=2022 and arrear<=2:
    if annual_income<=200000 and age >=18 and age<=21 and imarks>=60 and iattendance>=80:
        print("Eligible")
elif arrear>2:
    if imarks>80 and annual_income>200000 and annual_income<=250000 and age>=19 and age<=21 and iattendance>=90:
        print("Partially Eligible")
else:
    print("Not Eligible")

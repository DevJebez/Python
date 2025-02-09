time = "05:55:55AM"
if time[-2:] == "AM":
    if int(time[:2]) == 12:
        time="00"+time[2:8]
        print(time)
    else:
        print(time[:-2])

elif time[-2:] == 'PM':
    if int(time[:2]) == 12:
        print(time[0:8])
    else:
        print(str(int(time[:2])+12)+time[2:8])


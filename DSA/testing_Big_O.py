
import time
'''
# get the start time
st = time.process_time()

# main program
# find sum to first 1 million numbers
sum_x = 0
print("*")
print("**")
print("***")
print("****")
print("*****")



# get the end time
et = time.process_time()

# get execution time
res = et - st
print('CPU Execution time:', res, 'seconds')

'''


def current_milli_time():
    return round(time.time() * 1000)
startTime1 = current_milli_time()
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")
endTime1 = current_milli_time()


startTime2 = current_milli_time()
for i in range(1,35):
    print("*"*i)
endTime2 = current_milli_time()

print("Using print function, Time taken : ",endTime1 - startTime1)
print("Using iteration, Time taken : ",endTime2 - startTime2)





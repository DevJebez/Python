import random 
import string 

random_string = ''.join(random.choices(string.ascii_letters,k = 100000))

print(random_string)
roman = input("Enter roman")
roman_int = {"I" : 1 , "V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
i=0
res = 0
while i < len(roman):
    # check if current is less than next if so subract greatest - smallest 
    # Eg : IV 
    """ 
    here I < V so 5-1  = (4)
    """
    if i+1 < len(roman) and roman_int[roman[i]] < roman_int[roman[i +1]]:
        res += roman_int[roman[i+1]] - roman_int[roman[i]]
        i+=2 # skip the next element
    else:
        res += roman_int[roman[i]]
        i+=1
print(res)

"""
LVIII  --> 58

MCMXCIV --> 1994

"""

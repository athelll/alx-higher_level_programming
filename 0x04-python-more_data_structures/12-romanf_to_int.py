#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) != str) or (roman_string == None):
        return 0
    nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,}
    special = {'IV': 4, 'IX': 9,'XL': 40,'XC':90,'CD': 400, 'CM': 900}
    numsList = list(nums.keys())
    sums = 0
    for i, chars in enumerate(roman_string):
        for index, key in enumerate(numsList):
            if chars == key:
                if roman_string[i:(i+2)] in special:
                    sums -= nums.get(numsList[index+1])
                    sums += special[roman_string[i:(i+2)]]
                else:
                    sums += nums.get(key)
    return sums
print(roman_to_int('XXIV'))
print(roman_to_int('VII'))
print(roman_to_int('IX'))
print(roman_to_int('IV'))
print(roman_to_int('DCCVII'))
print(roman_to_int('LXXXVII'))
print(roman_to_int('MMMCMXCIX'))
print(roman_to_int('CM'))
print(roman_to_int('XC'))

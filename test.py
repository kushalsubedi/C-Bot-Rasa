
def roman_to_int(str)->int:
    str = str.upper()
    roman = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    val = 0
    for i in range (len(str)):
        if len(str)>(i+1) and roman.get(str[i+1]) > roman.get(str[i]):
            val -= roman.get(str[i])
        else:
            val += roman.get(str[i])

    return val

print (roman_to_int('iv'))
print (roman_to_int('vi'))
print (roman_to_int('v'))
print (roman_to_int('ix'))
print (roman_to_int('xx'))
print (roman_to_int('cm'))
print (roman_to_int('xD'))
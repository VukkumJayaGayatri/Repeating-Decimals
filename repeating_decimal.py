def repeating_decmials(numerator,denominator):
    if not (numerator, int) or not (denominator, int):
        raise ValueError("num and den must be integers")
def repeating_decimals(numerator, denominator): 
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise ValueError("Numerator and denominator must be integers")
    if denominator == 0:
        raise ValueError("den cannot be zero")
    result = ""
    remainder = numerator % denominator
    quotient = numerator // denominator
    result += str(quotient)
    if remainder == 0:
        return result
        raise ValueError("Denominator cannot be zero")
    result = "" 
    remainder = numerator % denominator 
    quotient = numerator // denominator 
    result += str(quotient) 
    if remainder == 0: 
        return result 
    result += "."
    remainders = {}
    if remainder == 0:
        return result
    result += "."
    remainders = {}
    while remainder != 0:
        if remainder in remainders:
    remainders = {} 
    while remainder != 0: 
        if remainder in remainders: 
            result = result[: remainders[remainder]]+result[remainders[remainder] :]
            return result
        remainders[remainder] = len(result)
        remainder *= 10
        quotient = remainder // denominator
        result += str(quotient)
        remainder %= denominator
    return result
            return result 
        remainders[remainder] = len(result) 
        remainder *= 10 
        quotient = remainder // denominator 
        result += str(quotient) 
        remainder %= denominator 
    return result 

try:
    numerator = int(input("enter a numerator:"))
    denominator = int(input("enter a denominator:"))
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(numerator,'/',denominator,'=',result)
    first, second = divmod(result, 1)
        for i in bar:
            print(i,end='')
        print()
        print('repeating',repeating_decimals(numerator, denominator))
        print('repeating',repeating_decimals(numerator, denominator))
except ValueError as e:
    print("Invalid input:", str(e))


def calculator_division(dividend,divisor): #300 divide by 901 here divisor is 300 and 901 is dividend
    quotient =0
    remainder =0
    if dividend ==0:
        return remainder,quotient
    elif divisor ==0:
        return "Infinity"
    while dividend>= divisor:
        dividend -= divisor
        quotient += 1
        remainder = dividend
        
        

    return quotient

user = float(input("Enter value one:"))
user1 = float(input("Enter value 2:"))
print(calculator_division(user,user1)) 

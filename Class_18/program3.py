"""
division

divident=jisko divide krna hy  5
divisor=jis se divide krna   55
quotient=
remainder=
"""
def calculator_division(dividend,divisor): #300 divide by 901 here divisor is 300 and 901 is dividend
    quotient =0
    remainder =0
    if dividend ==0:
        return quotient
    elif divisor ==0:
        return "Infinity"
    while dividend>= divisor:
        dividend -= divisor
        quotient += 1
        remainder = dividend
    return quotient


    

def calculator_square_root(number):
    number = 0
    if number < 0:
        print("Error! Try Again")
    suppose = number
    d= calculator_division(number,suppose)
    var = suppose + d
    result = calculator_division(var,2)

    iterations = 1000
    for i in range(1000):
        new = result
    return new

     
u_1 = int(input("Enter the value:"))
print(calculator_square_root(u_1))
"""
formula for this:
formula = (suppose + number/suppose)/2
"""


"""
if remainder <= 0 or remainder <= divisor:
            print("remainder:",remainder)
"""
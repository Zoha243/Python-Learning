# Using functions making an Calculator project:
# in which division and multiplication can not be done direct!

def Calculator_sum(a,b):
    sum = a+b
    return sum

#print("Function for Subtraction")
def calculator_Subtract(x,y):
    subtract = x-y
    return subtract

# 2 * 5
#print("Function for Multiplication")
def calculator_multiplication(num1,num2):
    var = 0
    for i in range(num2):
       var = var + num1
    return var


#print("Function for Factorial")
def calculator_factorial(n1):
    var=1
    for i in range(n1,0,-1):
        var = calculator_multiplication(var,i)
    return var



def calculator_division(dividend,divisor,precision=3): #300 divide by 901 here divisor is 300 and 901 is dividend
    result = []
    int_part = 0
    remainder = dividend #5
    while remainder >= divisor: #5 >= 3
        remainder -= divisor
        int_part += 1 

    result.append(str(int_part))
    remainder *= 10 #20
    result.append('.')  # Add decimal point

    for i in range(precision):
        quotient = 0
        while remainder >= divisor:
            remainder -= divisor #17,14,11,8,5,2
            quotient += 1  #1,2,3,4,5,6

        remainder *= 10
        result.append(str(quotient))

    result_str = ''.join(result)
    return result_str

def calculator_square_root(number):
    for i in range(number):
        if calculator_multiplication(i,i)==number:
            print("Square root of is:",i)
            break
        elif calculator_multiplication(i,i)>number:
            print("Not a perfect square!")
            break

var= True
while var:
    print("Calculator")
    print("press 1 for Addition")
    print("press 2 for Subtraction")
    print("press 3 for Multiplication")
    print("press 4 for Division")
    print("press 5 for Factorial")
    print("press 6 for Square root")
    Person= int(input("Choice:"))
    if Person ==1:
        user=int(input("Enter Value of a:\n"))
        user_1=int(input("Enter Value of b:\n"))
        print("Sum:",Calculator_sum(user,user_1))
    elif Person ==2:
        u=int(input("Enter Value of x:\n"))
        u_1=int(input("Enter Value of y:\n"))
        print("subtraction:",calculator_Subtract(u,u_1))
    elif Person ==3:
        u=int(input("Enter Value of num1:\n"))
        u_1=int(input("Enter Value of num2:\n"))
        print("Multiplication:",calculator_multiplication(u,u_1))
    elif Person ==4:
        user = float(input("Enter value one:"))
        user1 = float(input("Enter value 2:"))
        print(calculator_division(user,user1)) 
    elif Person ==5:
        uu=int(input("Enter Value of num1:\n"))
        print("factorial:",calculator_factorial(uu))
    elif Person==6:
        u_1 = int(input("Enter the value:"))
        calculator_square_root(u_1)
        #print("Square Root",calculator_square_root(u_1))
    Person_2=input("Do You want to perform calculations Again Press yes for continue and No for Exit \n")
    if Person_2 == "Yes" or Person_2 == "yes":
        var = True
    elif Person_2 == "No" or Person_2 == "no":
        var = False





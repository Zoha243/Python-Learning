# Check Valid Triangle
a=int(input("Value of a\n"))
b=int(input("Value of b\n"))
c=int(input("Value of c\n"))

x= a+b
y = a+c
z= b +c
if x>c and y>b and z>a:
    print("its an Triangle")
else:
    print("Not a Triangle")
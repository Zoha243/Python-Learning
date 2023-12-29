# Determine Quadrant of a Coordinate
x =int(input("Value for X\n"))
y = int(input("Value for Y\n"))
if x>0 and y>0:
    print("point lies in the first quadrant")
if x<0 and y>0:
    print("point lies in the Second quadrant")
if x<0 and y<0:
    print("point lies in the third quadrant")
if x>0 and y<0:
    print("point lies in the fourth quadrant")

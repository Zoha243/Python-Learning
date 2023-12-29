"""


A = {1,2,3,4}
B = {1,2,3,4}
AxB = {(1,1),(1,2),(1,3),(1,4)}
5X5 
7x7 
***  
*   *
*   *
*   *
***


    *
   **
  *
 **
***

5)123(24.6 
  10 
__
23
20
___
3

300)901(3.003
    900
    __
    1000
    900
    __
    100


"""

# side = 5
# print("*"*side)
# for i in range(side-2):
#     print(""+" "(side-2)+"*")
# print("*"*side)

# len = 12
# for i in range(1,(len+1)):
#     print((len-i)" "+i"*")

# print(" "4+""*(1))
# print(" "3+""*(2))
# print(" "2+""*(3)) 
# print(" "1+""*(4))
# print(" "0+""*(5))
length = 5
even = 2
count = 3
# print(" "length-1+"")
# for i in range(length-2,0,-1):
for i in range(3):
    print(count,even)
    count-=1
    even+=2
for i in range(3):
    even-=2    
    count+=1
    print(count,even)    
# for i in range(1,length-1,):
#     even-=2
#     print(i,even)
    
# print(" "length-1+"")
# print(2,4)
# print(1,6)
# Given an array of ints, return True if 6 appears as either the first or last element in the array.
# The array will be length 1 or more.
#first_last6([1, 2, 6]) → True
#first_last6([6, 1, 2, 3]) → True
#first_last6([13, 6, 1, 2, 3]) → False

list1 =[1,2,3,6]
print(list1[3]==6)

list3 =[6, 1, 2, 3]
print(list3[0]==6)

first_last6=[13, 6, 1, 2, 3]
print(first_last6[0]==6 , first_last6[4]==6)
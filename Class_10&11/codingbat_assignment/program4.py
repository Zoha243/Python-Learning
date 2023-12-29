# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
# The string length will be at least 2.

str1 = "Hello"
print(str1[len(str1)-2:]*3)
str2 ="ab"
print(str2[len(str2)-2:]*3)
str3 = "hi"
print(str3[len(str3)-2:]*3)

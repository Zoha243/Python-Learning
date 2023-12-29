# setdefault() Returns the value of the specified key. 
# If the key does not exist: insert the key, with the specified value.


# Syntax: dict.setdefault(key, default_value)
# Parameters: It takes two parameters: 

dict1 = {'Maths': 97, 'Physics': 98, 'chemistry': 99, 'data Science': 100} 
# space key added using setdefault() method 
dict1.setdefault(' ', 87) 
print(dict1)



d = {'a': 97, 'b': 98} 
print("setdefault() returned:", d.setdefault('b', 99)) 
print("After using setdefault():", d)
# Wont modify the dictionary
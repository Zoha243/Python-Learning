# isascii()  True if all the characters are ascii characters  (a-z).
#Return True if the string is empty or all characters in the string are ASCII, False otherwise.

text="12334students"
print(text.isascii())
 
text1="This contains non ASCII characters こんにちは"  # its output should be false! 
print(text1.isascii())
    
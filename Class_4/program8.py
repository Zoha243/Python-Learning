#  The find() method should be used only if you need to know the position of sub.  Return -1 if sub is not found.
sentence= "Hello, zoha here!"
# now if i want to see the index of letter z that's how we can use it
print(sentence.find("z"))
print(sentence.find("k"))

# if i want to check the index of e from the last word here:
print(sentence.find("e",11,17))
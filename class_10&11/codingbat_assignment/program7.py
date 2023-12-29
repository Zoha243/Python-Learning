# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
 
tag = "<i></i>"
str = "yay"
print(tag[:3]+"yay"+tag[3:])

#make_tags('cite', 'Yay') → '<cite>Yay</cite>'
tag2 = "<></>"
print(tag2[:1]+"cite"+tag2[1:3]+"cite"+tag2[3:])
# dynamic logic!!!

#code:1
import re
string = "bc"
pattern = "a"
if re.match(pattern,string):
    print("Match found")
else:
    print("No Match found")

#code:2
import re
text = "The sentence includes punctuations! \n"
pattern = r'\W'
matches = re.findall(pattern,text)
print(matches)
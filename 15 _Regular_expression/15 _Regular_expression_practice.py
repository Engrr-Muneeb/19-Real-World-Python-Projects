#code:1
import re

text = "Date: 20223-06-08  1990-01-02"
pattern = r"\d{4}-\d{2}-\d{2}"

dates = re.findall(pattern,text)
print(dates)

#code:2
import re

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A.Za-z]{2,}\b"
email = input("Enter email address\n")

if re.match(pattern,email):
   print("Valid email")
else:
   print("Invalid email")
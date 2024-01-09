#code#1
file = open("C:\\Users\\asmam\\Documents\\work\\19-Real-World-Python-Projects\\11_file _handling\\data.txt" , 'r')
content = file.readline()
print(content)
file.close()
#code#2
file = open("C:\Users\asmam\Documents\work\19-Real-World-Python-Projects\11_file _handling\data.txt" , 'a')
content = "This is fourth line"
file.write(content)
file.close()

with open("C:\\Users\\asmam\\Documents\\work\\19-Real-World-Python-Projects\\11_file _handling\\data.txt" , 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
#code#3
while True:
    with open("name.txt","a") as file:
      name = input("Enter name to be added: ")
      file.write(name + '\n')
      choice = input("Do you want to add more names? (y/n)")
      if choice == 'n':
         break
with open("name.txt","r") as file:
   lines = file.readlines()#for line in lines:
   print(line.strip().capitalize())

#code#4
def save_user_data():
    name = input("Enter your name\n")
    email = input("Enter your email\n")
    contact = input("Enter your contact number\n")

    user_data = F"Name: {name}\nEmail: {email}\ncontact: {contact}\n"
    with open("user_data.txt","a") as file:
        file.write(user_data)

def read_user_data():
    with open("user_data.txt","r") as file:
        print(file.read())

save_user_data()
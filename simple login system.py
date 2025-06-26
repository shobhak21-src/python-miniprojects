def register():
  username=input("enter username")
  password=input("enter password")
  with open("users.txt","r") as file:
       for line in file:
           saved_username, _= line.strip().split(":")
           if saved_username==username:
            print("user already exist")
            return
        
  with open("user.txt","a") as file:
    file.write(f"{username}:{password}\n")
  print("Registration succesful!")

def login():
   username=input("enter username")
   password=input("enter password")
   with open("users.txt","r") as file:
     for line in file:
      saved_username,saved_password=line.strip().split(":") 
      if saved_username == username and saved_password == password:
         print("Login Successfull")
         return
print("Invalid Username or Password") 
def main():
   while True:
       print("\n===== Login System =====")  
       print("1. Register")       
       print("2. Login")
       print("3. Exit")
       choice = input("choose an option(1/2/3):")
       if choice == '1':
         register()
       elif choice == '2':
         login()
       elif choice == '3':
         print("exiting... goodbye!")
         break
   else:
         print("invalid choice. Try Again.")  
main()                   
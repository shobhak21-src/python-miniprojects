def create_user_card(name,age,email,phone,address):
    print("\n" + "-"*31)
    print("|{:^31}|".format("USER INFO CARD"))
    print("-"*31)
    print(f"|name    :  {name:<20}|")
    print(f"|Age     :  {age:<50}|")
    print(f"|Email   :  {email:<20}|")
    print(f"|Phone   :  {phone:<10}|")
    print(f"|Address :  {address:<20}|")
    print("-"*31)

name =input("enter your name:")
age =input("enter your age:")

email =input("enter your email:")
phone =input("enter your phone:")

address =input("enter your address:")

def is_valid_email(email):
    return email.endswith("@gmail.com") and "@" in email and not email.startswith("@")



if not age.isdigit():
    print("invalid age!Please enter a number.")
elif not (phone.isdigit() and len(phone)==10):
    print("invalid phone!Please enter a number.")
elif not is_valid_email(email):  
    print("Invalid email address! Only valid Gmail addresses are allowed.")

    
else:    
    create_user_card(name,age,email,phone,address)
    
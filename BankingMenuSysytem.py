balance = 50000
running = True
while running:

   print("\n =======WELCOME TO MY BANK=======")
   print("1. check balance")
   print("2. Deposit Money")
   print("3. Withdraw Money")
   print("4. Exit")

   choice =int(input("enter your coice (1-4): "))

   if choice == 1:
     print(f"your current balance is Rs{balance}")
   elif choice == 2:
     amount=int(input("enter amount to be deposit:"))
     balance += amount
     print(f"Rs{amount} deposited succesfully.")
     print(f"Rs{balance} is total balance in your account")
   elif choice == 3:
     amount=int(input("enter amount  to withdraw"))
     if amount <= balance:
      balance -= amount
      print(f"Rs.{amount} withdraw succesfully")
      print(f"Rs{balance} is total balance  left in your account")
     else:
      print(" Insufficient balance")
   elif choice == 4:
      print("Thank you! Have a nice day")

      running = False

   else:
       print("Wrong choice please select between (1-4)")   
  


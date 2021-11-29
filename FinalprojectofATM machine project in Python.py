import time
print("     " "Welcome to Harsha Banking Atm""      ")
time.sleep(2)
print("enter your details for creating a bank atm")
time.sleep(2)
a=input("enter your name:")
b=int(input("enter your mobile number:"))
c=input("enter a valid pin for atm:")
print("Please insert Your CARD")
#for card processing
time.sleep(3)
print("Thank you for inserting your card")
time.sleep(2)
print("welcome"+" "+a)
time.sleep(2)
balance = 0
pin = input("enter your atm pin:")
if pin == c:
    while True:
        print(""" 
			1 == balance
			2 == withdraw balance
			3 == deposit balance
			4 == exit
			"""
              )
        try:    
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter valid option")  
        if option == 1:
            print(f"Your current balance is {balance}")                                     
        elif option == 2:
            withdraw_amount = int(input("please enter withdraw_amount "))
            if withdraw_amount < balance:
                balance = balance - withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"your updated balance is {balance}")
            else:
                print("insufficientfunds")
        elif option == 3:
            deposit_amount = int(input("please enter deposit_amount"))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"your updated balance is {balance}")
        elif option == 4:
            break


else:
    print("wrong pin Please try again")


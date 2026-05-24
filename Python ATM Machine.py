print("------------Welcome to Python ATM Machine---------------")
balance=1000
pin=9876
transaction_history=[]
for pinattempts in range(3):
    enter_pin=int(input("enter your 4 digit atm pin: "))
    if enter_pin==pin:
        print("Login Successfull")
        break
    else:
        print("Invalid pin")
else:
    print("Too many wrong attempts, account locked")
    exit()

def balance_enquiry():
    print(f"your current balance is: {balance}")
def desposit():
    global balance
    deposit_amount=int(input("enter your amount: "))
    balance+=deposit_amount
    transaction_history.append(f"{deposit_amount} is successfully deposited")
    print(f"Your Updated Balance is: {balance}")
def withdrawl():
    global balance
    withdrawl_amount=int(input("enter withdrawl amount: "))
    if withdrawl_amount<balance:
        balance-=withdrawl_amount
        transaction_history.append(f"{withdrawl_amount} is withdrawn")
        print(f"{withdrawl_amount} is successfully withdrawn, \nyour updated balance is: {balance}")
    else:
        print("your balance is insufficient")
def transactions():
    if transaction_history==0:
        print("no transactions yet!")
    else:
        print("\nTransaction History:")
        for transaction in transaction_history:
            print(transaction)
while True:
    print("-----Select your choice------")
    print("-----Select 1 for balance_enquiry------")
    print("-----Select 2 for deposit------")
    print("-----Select 3 for withdrawl------")
    print("-----Select 4 for transactions_history------")
    print("-----Select 5 for exit------")
    
    enter_your_choice=int(input("enter your choice: "))
    if enter_your_choice==1:
        balance_enquiry()
    elif enter_your_choice==2:
        desposit()
    elif enter_your_choice==3:
        withdrawl()
    elif enter_your_choice==4:
        transactions()
    elif enter_your_choice==5:
        print("Thanks for using Python ATM Machine")
        break
    else:
        print("Invalid option, try again")






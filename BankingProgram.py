# 1. Show Balance
# 2. Deposit
# 3. Withdraw

def show_balance(balance):
    print(f"Your balance is Rs{balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("Not a valid amount!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient Balance!")
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*****************")
        print(" BANKING PROGRAM ")
        print("*******************")
        print("1. SHOW BALANCE")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. EXIT")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Not a valid choice!")

    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()

#Banking System
def display_menu():
    print("\nWelcome to Your Bank Account!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit(balance):
    try:
        amount = float(input("Enter the amount to deposit: $"))
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        balance += amount
        print(f"${amount:.2f} has been deposited. Your new balance is: ${balance:.2f}")
        return balance
    except ValueError as e:
        print(f"Error: {e}")
        return balance

def withdraw(balance):
    try:
        amount = float(input("Enter the amount to withdraw: $"))
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > balance:
            raise ValueError("Insufficient balance!")
        balance -= amount
        print(f"${amount:.2f} has been withdrawn. Your new balance is: ${balance:.2f}")
        return balance
    except ValueError as e:
        print(f"Error: {e}")
        return balance

def main():
    balance = 1000.00  
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Choose an option (1-4): "))
            if choice == 1:
                check_balance(balance)
            elif choice == 2:
                balance = deposit(balance) 
            elif choice == 3:
                balance = withdraw(balance) 
            elif choice == 4:
                print("Thank you for using our services. Goodbye!")
                break  
            else:
                print("Invalid choice. Please choose a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


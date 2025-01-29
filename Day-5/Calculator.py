#Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def display_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter choice (1/2/3/4/5): "))
            if choice == 5:
                print("Exiting the calculator. Goodbye!")
                break
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == 1:
                print(f"The result of addition is: {add(num1, num2)}")
            elif choice == 2:
                print(f"The result of subtraction is: {subtract(num1, num2)}")
            elif choice == 3:
                print(f"The result of multiplication is: {multiply(num1, num2)}")
            elif choice == 4:
                print(f"The result of division is: {divide(num1, num2)}")
            else:
                print("Invalid input. Please choose a valid operation.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

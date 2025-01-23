def perform_operation():
    try:
        num1 = 10
        num2 = 5
        result = num1 / num2
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    finally:
        print("Operation is complete.")

perform_operation()

print()


def perform_operation():
    try:
        num1 = 10
        num2 = 0
        result = num1 / num2 
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    finally:
        print("Operation is complete.")
perform_operation()

#Vegetables example
def check_vegetable(vegetable, available_vegetables):
    try:
        if vegetable not in available_vegetables:
            raise ValueError(f"{vegetable} is not in stock!")
        else:
            print(f"{vegetable} is available in stock.")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Operation is complete.")

vegetables_in_stock = ["carrot", "potato", "tomato"]

check_vegetable("carrot", vegetables_in_stock)

print()

check_vegetable("broccoli", vegetables_in_stock)

print()

check_vegetable("2",vegetables_in_stock)

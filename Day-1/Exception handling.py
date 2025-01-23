#Exception Handling

#Zero Division Error
def numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"

num1 = int(input("Enter first number"))
num2 = int(input("Enter the second number"))
print(numbers(num1, num2))

#Value Error
def add_numbers(num1, num2):
    try:
        result = int(num1) + int(num2)
        return result
    except ValueError:
        return "Error: Both inputs must be valid numbers!"
print(add_numbers("10", "5"))
print(add_numbers("10", "abc"))
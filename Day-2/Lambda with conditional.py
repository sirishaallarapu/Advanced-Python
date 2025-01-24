# Lambda function to check if a number is even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"
num = int(input("Enter the number : "))
result = check(num)
print(f"The number {num} is {result}")

# Lambda function to check if a number is greater than 10
check_greater_than_10 = lambda x: "Yes" if x > 10 else "No"
num = int(input("Enter the number : "))
result = check_greater_than_10(num)
print(f"Is {num} greater than 10? {result}")


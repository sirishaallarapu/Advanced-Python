#Lambda function
multiply = lambda x, y: x * y
add = lambda x, y: x + y

num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

result1 = multiply(num1, num2)
result2 = add(num1, num2)

print(f"The product of {num1} and {num2} is {result1}")
print(f"The sum of {num1} and {num2} is {result2}")



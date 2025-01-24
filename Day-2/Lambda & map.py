#Sqaure of list
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)

squared_numbers_list = list(squared_numbers)
print(f"Squared numbers: {squared_numbers_list}")

#Add 2 to each number
numbers = [1, 2, 3, 4, 5]
updated_numbers = map(lambda x: x + 2, numbers)

updated_numbers_list = list(updated_numbers)
print(f"Numbers after adding 2: {updated_numbers_list}")

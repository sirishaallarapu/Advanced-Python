# Try and catch exceptions

# Index error
string = input("enter the string name")
index = int(input("enter the index"))

try:
    char = string[index]
    print(char)
except IndexError:
    print("Error: Index is out of range!")

#Accessing an out of range Index in a List:

my_list = [10, 20, 30, 40, 50]

try:
    print(my_list[10])
except IndexError:
    print("Error: Index is out of range!")
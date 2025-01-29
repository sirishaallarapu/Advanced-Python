def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def display_menu():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-3): "))
            
            if choice == 1:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
            elif choice == 2:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option (1-3).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

def display_menu():
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Sort Products by Price")
    print("5. Sort Products by Quantity")
    print("6. Generate Report")
    print("7. Exit")

def add_product(products):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    products.append({"name": name, "price": price, "quantity": quantity})
    print(f"Product '{name}' added successfully.")

def view_products(products):
    if products:
        print("\nProduct List:")
        for product in products:
            print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
    else:
        print("No products in the inventory.")

def search_product(products):
    search_name = input("Enter product name to search: ")
    found = False
    for product in products:
        if search_name.lower() in product['name'].lower():
            print(f"Found Product - Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
            found = True
    if not found:
        print(f"No product found with the name '{search_name}'.")

def sort_products_by_price(products):
    sorted_products = sorted(products, key=lambda x: x['price'])
    print("\nProducts sorted by price:")
    for product in sorted_products:
        print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

def sort_products_by_quantity(products):
    sorted_products = sorted(products, key=lambda x: x['quantity'])
    print("\nProducts sorted by quantity:")
    for product in sorted_products:
        print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

def generate_report(products):
    print("\nInventory Report:")
    if products:
        total_value = sum(product['price'] * product['quantity'] for product in products)
        print(f"Total Inventory Value: {total_value}")
        print("Product Breakdown:")
        for product in products:
            print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
    else:
        print("No products in the inventory to generate a report.")

def main():
    products = []
    
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-7): "))
            
            if choice == 1:
                add_product(products)
            elif choice == 2:
                view_products(products)
            elif choice == 3:
                search_product(products)
            elif choice == 4:
                sort_products_by_price(products)
            elif choice == 5:
                sort_products_by_quantity(products)
            elif choice == 6:
                generate_report(products)
            elif choice == 7:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a valid option (1-7).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

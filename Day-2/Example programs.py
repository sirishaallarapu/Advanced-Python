#Example1
products = [
    {"name": "Laptop", "price": 900},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300},
]
sorted_products = sorted(products, key=lambda x: x['price'])
print(sorted_products)

#Example2
fruits = ["apple", "banana", "kiwi", "orange", "pear"]
filtered_fruits = list(filter(lambda x: len(x) > 5, fruits))
print(filtered_fruits)

#Example3
vegetables = [("Carrot", 2.5), ("Tomato", 3.5), ("Cucumber", 2.0), ("Potato", 4.0)]
expensive_vegetables = list(filter(lambda x: x[1] > 3, vegetables))
print(f"Vegetables with price greater than 3: {expensive_vegetables}")

#Example4
from datetime import datetime
products = [
    {"name": "Milk", "expiry": "2025-01-25"},
    {"name": "Cheese", "expiry": "2025-02-10"},
    {"name": "Butter", "expiry": "2025-01-20"},
]
today = datetime.now().strftime('%Y-%m-%d')
expired_products = list(filter(lambda x: x['expiry'] < today, products))
print(expired_products)




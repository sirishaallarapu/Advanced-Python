#Car Example
class Car:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")
        print(f"Mileage: {self.mileage} miles")

    def drive(self, miles):
        self.mileage += miles
        print(f"Driving {miles} miles. New mileage: {self.mileage} miles")
    def service(self):
        print(f"Servicing the {self.make} {self.model}.")
        self.mileage = 0

my_car = Car("Suzuki","Ignis", 2025)

my_car.display_info() 

my_car.drive(200)

my_car.display_info()

my_car.service()

my_car.display_info()


#Vegetable example
class Vegetable:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def display_info(self):
        print(f"Vegetable: {self.name}")
        print(f"Color: {self.color}")
        print(f"Weight: {self.weight} grams")

    def is_fresh(self):
        if self.weight > 100:
            print(f"{self.name} is fresh!")
        else:
            print(f"{self.name} is not fresh yet.")

    def compare_weight(self, other_vegetable):
        if self.weight > other_vegetable.weight:
            print(f"{self.name} is heavier than {other_vegetable.name}.")
        elif self.weight < other_vegetable.weight:
            print(f"{self.name} is lighter than {other_vegetable.name}.")
        else:
            print(f"{self.name} and {other_vegetable.name} weigh the same.")

carrot = Vegetable("Carrot", "Orange", 150)
tomato = Vegetable("Tomato","Red",80)
carrot.display_info() 
tomato.display_info()






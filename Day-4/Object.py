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
        print(f"Servicing the {self.make} {self.model}... Mileage reset.")
        self.mileage = 0

my_car = Car("Toyota", "Fortuner" , 2025)
my_car.display_info()
my_car.drive(150)
my_car.display_info()
my_car.service()
my_car.display_info()

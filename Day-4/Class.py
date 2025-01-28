#Person class
class Person:
   def __init__(self, name):
        self.name = name

person1 = Person("Siri")

print(person1.name)

#Student Class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
    
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(f"Updated Grade for {self.name}: {self.grade}")

    def is_passing(self):
        if self.grade >= 60:
            return True
        else:
            return False
        
student1 = Student("Siri", 16, 85)
student1.display_info()

student1.update_grade(90)

if student1.is_passing():
    print(f"{student1.name} is passing!")
else:
    print(f"{student1.name} is not passing.")





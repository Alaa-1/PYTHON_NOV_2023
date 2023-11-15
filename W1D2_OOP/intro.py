# / OOP
# ? Object?
name = "sport"
age = 3
breed = "someBreed"
color = "Black"
dog1 = {"name": name, "age": age, "breed": breed, "color": color}
dog2 = {"name": "Sprak", "age": 2, "breed": "labrador", "color": "Brown"}

# DRY
# Don't Repeart Yourself


# ? CLASS?
# ------ CREATE A CLASS --------
class Dog:
    # Constructor - creates defaults and builds the instance
    def __init__(self, name, age, breed, color):
        # ? attributes
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

    def bark(self):
        print(f"{self.name} is barking - WOOOF !")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name} you are {self.age} years old 🥳 ")


# Create an instance (object)
# Instantiate a class
# myDog = Dog()

# print(myDog)
# print(myDog.name)
# myDog.bark()

yourDog = Dog("Bobby", 6, "unknown", "Golden")
dog2 = Dog("Marshal", 1, "Golden Retriever", "Golden")

print(yourDog.name)  # Bobby
print(dog2.name)  # Marshal
yourDog.bark()
dog2.bark()

dog2.birthday()

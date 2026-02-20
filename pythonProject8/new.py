class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

my_dog = Dog("Buddy", "Golden Retriever", 3)

print(f"{my_dog.name} is {my_dog.age} years old.")
my_dog.bark()
my_dog.birthday()
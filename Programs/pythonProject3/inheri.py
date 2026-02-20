class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def description(self):
        return f"This car is a {self.brand} from {self.year}."

class Car(Vehicle):
    def __init__(self, brand, year, seats):
        super().__init__(brand, year)
        self.seats = seats

    def description(self):
        parent_desc = super().description()
        return parent_desc + f" It has {self.seats} seats."

class Bus(Vehicle):
    def __init__(self, brand, year, capacity):
        super().__init__(brand, year)
        self.capacity = capacity

    def description(self):
        parent_desc = super().description()
        return parent_desc + f" It can carry {self.capacity} passengers."

car = Car("Nissan", 2020, 4)
bus = Bus("Scania", 2021, 56)

print(car.description())
print(bus.description())

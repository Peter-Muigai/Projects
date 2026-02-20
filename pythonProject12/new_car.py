"""A class that can be used to represent a car."""
class Car:
    """A simple attempt to model a car."""
    def __init__(self, make, model, year):
        """Initialize attributes of the car."""
        self.make =make
        self.model =model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def reading_odometer(self):
        """Print a statement showing the odometer reading for the car."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer to the given value.
        Reject the change if attempts to roll back the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer.")

    def increment_reading(self, miles):
        """Add miles to the odometer."""
        self.odometer_reading += miles


my_new_car = Car('audi', 'q4', 2023)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(24000)
my_new_car.reading_odometer()

my_new_car.increment_reading(100)
my_new_car.reading_odometer()
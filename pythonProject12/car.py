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

my_new_car = Car('audi', 'q4', 2023)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 24
my_new_car.reading_odometer()
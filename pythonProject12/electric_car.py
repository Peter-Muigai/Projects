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

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size} KWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about a {range} miles on full battery")


class ElectricCar(Car):
    """Represents aspects of a car specific to an electric car."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()


my_new_car = ElectricCar('Tesla', 'model f5', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.battery.describe_battery()
my_new_car.battery.get_range()
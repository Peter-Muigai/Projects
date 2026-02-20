class Restaurant:
    """A Simple restaurant."""

    def __init__(self, name, types):
        """Initialize restaurant name and salad"""
        self.name = name
        self.types = types

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"The {self.name} is located on the 5th Avenue.")
        print("Welcome all to this amazing place.")

    def open_restaurant(self):
        """Show that restaurant is now open."""
        print(f"{self.name} is now open.")

my_restaurant = Restaurant('PEMU', 'beverages')
your_restaurant = Restaurant('FELIZ', 'wines')

print(f"Welcome to {my_restaurant.name} we serve {my_restaurant.types}.")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(f"\nWelcome to {your_restaurant.name} they serve {your_restaurant.types}")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()
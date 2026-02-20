class Restaurant:
    """A Simple restaurant."""

    def __init__(self, name, salad):
        """Initialize restaurant name and salad"""
        self.name = name
        self.salad = salad
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"\nThe {self.name}is located on the 5th Avenue.")
        print("\nWelcome all to this amazing place.")

    def open_restaurant(self):
        """Show that restaurant is now open."""
        print(f"\n{self.name} is now open.")

    def restaurant(self):
        """Print the number of customers served."""
        print(f"The restaurant has served {self.number_served} customers.")

    def set_number_served(self, customers):
        """Set the number of customers served."""
        self.number_served = customers

    def increment_number_served(self, customers):
        """Increase the number of customers served."""
        self.number_served += customers

my_restaurant = Restaurant('PEMU', 'vegan')
my_restaurant.set_number_served(21)
my_restaurant.increment_number_served(5)
print(f"Welcome to {my_restaurant.name} we serve {my_restaurant.salad}.")
my_restaurant.restaurant()

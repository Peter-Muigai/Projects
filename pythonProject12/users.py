class User:
    """A simple user-based profile."""
    def __init__(self, first_name, last_name, height, age):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.age = age

    def describe_user(self):
        """Print out a description of the user."""
        user_profile = f"""
First name:{self.first_name}     
Last name:{self.last_name}
Height: {self.height}
Age: {self.age}
                        """
        return user_profile.title()
    def greet_user(self):
        """Print out a personalized greeting to user."""
        print(f"Good day {self.first_name} {self.last_name}!")

my_name = User('Peter', 'Muigai', 4.5, 21)
your_name = User('John', 'Mai', 5.8, 24)

print(f"{my_name.describe_user()}")
print(f"{your_name.describe_user()}")

my_name.greet_user()
your_name.greet_user()
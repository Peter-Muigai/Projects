class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.lives = 9

    def meow(self):
        print(f"{self.name} says Meow!")

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            print(f"Too bad for {self.name}! She now has {self.lives} lives left.")
        else:
            print(f"{self.name} has no lives left.")

    def status(self):
        print(f"{self.name} is a {self.colour} cat with {self.lives} lives.")


my_cat = Cat("Whiskers", "black & white")
print(f"{my_cat.name} has {my_cat.lives} lives now.")
my_cat.meow()
my_cat.lose_life()
my_cat.status()

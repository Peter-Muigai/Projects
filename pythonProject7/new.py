class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price  

    def describe(self):
        print(f"This book is {self.title} by {self.author}.")

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

book = Book("Atomic Habits", "James Clear", 1000)
book.describe()
print("Price:", book.get_price())
book.set_price(-500)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


    def describe(self):
        print(f"This book is {self.title} by {self.author}.")
b = Book("Atomic Habits", "James Clear")
b.describe()

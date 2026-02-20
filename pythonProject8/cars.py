class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            print("Engine started.")
        else:
            print("Engine is already running.")

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            print("Engine stopped.")
        else:
            print("Engine is already off.")

    def drive(self, km):
        if self.engine_on:
            self.mileage += km
            print(f"You drove {km} km. Total mileage is {self.mileage} km.")
        else:
            print("Can't drive. The engine is off.")


    def status(self):
        engine_state = "on" if self.engine_on else "off"
        print(
         f'This is a {self.brand} {self.model} ({self.year}) with {self.mileage} km mileage. Engine is {engine_state}.')

my_car = Car("Toyota", "Corolla", 2022)
my_car.status()
my_car.drive(10)
my_car.start_engine()
my_car.drive(10)
my_car.status()
my_car.stop_engine()

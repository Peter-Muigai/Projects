from abc import ABC, abstractmethod

# Abstract Base Class
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Light appliance
class Light(Appliance):
    def __init__(self):
        self.__state = False  # Encapsulated state (off)

    def turn_on(self):
        self.__state = True
        print("Light turned on.")

    def turn_off(self):
        self.__state = False
        print("Light turned off.")

# Fan appliance
class Fan(Appliance):
    def __init__(self):
        self.__state = False  # Encapsulated state (off)

    def turn_on(self):
        self.__state = True
        print("Fan spinning.")

    def turn_off(self):
        self.__state = False
        print("Fan stopped.")

# SmartHomeController
class SmartHomeController:
    def __init__(self):
        self.__appliances = []  # List to hold all appliances

    def add_appliance(self, appliance: Appliance):
        self.__appliances.append(appliance)

    def activate_all(self):
        for appliance in self.__appliances:
            appliance.turn_on()

    def deactivate_all(self):
        for appliance in self.__appliances:
            appliance.turn_off()

# Create appliances
light1 = Light()
fan1 = Fan()

# Create controller and add appliances
controller = SmartHomeController()
controller.add_appliance(light1)
controller.add_appliance(fan1)

# Activate all
controller.activate_all()

# Deactivate all
controller.deactivate_all()

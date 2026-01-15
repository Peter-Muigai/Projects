from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def status(self):
        pass

class Light(Appliance):
    def __init__(self):
        self.__state = False

    def turn_on(self):
        self.__state = True
        print("Light turned on.")

    def turn_off(self):
        self.__state = False
        print("Light turned off.")

    def status(self):
        return "Light is ON" if self.__state else "Light is OFF"

class Fan(Appliance):
    def __init__(self):
        self.__state = False

    def turn_on(self):
        self.__state = True
        print("Fan spinning.")

    def turn_off(self):
        self.__state = False
        print("Fan stopped.")

    def status(self):
        return "Fan is ON" if self.__state else "Fan is OFF"

class SmartHomeController:
    def __init__(self):
        self.__appliances = []

    def add_appliance(self, appliance: Appliance):
        self.__appliances.append(appliance)

    def activate_all(self):
        for appliance in self.__appliances:
            appliance.turn_on()

    def deactivate_all(self):
        for appliance in self.__appliances:
            appliance.turn_off()

    def show_status(self):
        print("\n📡 Smart Home Status:")
        for appliance in self.__appliances:
            print("•", appliance.status())

# Create devices
light = Light()
fan = Fan()

# Create controller
controller = SmartHomeController()
controller.add_appliance(light)
controller.add_appliance(fan)

# Control appliances
controller.activate_all()
controller.show_status()

controller.deactivate_all()
controller.show_status()

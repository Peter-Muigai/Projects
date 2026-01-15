from abc import ABC, abstractmethod


class Appliance(ABC):
    @abstractmethod
    def turn_on(self, up):
        pass

    def turn_off(self, down):
        pass

class Light(Appliance):
    def __init__(self, on):
        self.__on = on

    def turn_on(self, up):
        if self.__on == up:
            print("On")
        else:
            print("Off")

    def turn_off(self, down):
        if self.__on == down:
            print("Off")
        else:
            print("On")

class Fan(Appliance):
    def __init__(self, on):
        self.__on = on

    def turn_on(self, up):
        if self.__on == up:
            print("On")
        else:
            print("Off")

    def turn_off(self, down):
        if self.__on == down:
            print("Off")
        else:
            print("On")

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

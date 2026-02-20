from abc import ABC, abstractmethod

# Abstract Base Class
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

# Light Appliance
class Light(Appliance):
    def __init__(self, name="Light"):
        self.__state = False
        self.__name = name

    def turn_on(self):
        self.__state = True
        print(f"{self.__name} turned on.")

    def turn_off(self):
        self.__state = False
        print(f"{self.__name} turned off.")

    def status(self):
        return f"{self.__name} is ON" if self.__state else f"{self.__name} is OFF"

# Fan Appliance
class Fan(Appliance):
    def __init__(self, name="Fan"):
        self.__state = False
        self.__name = name

    def turn_on(self):
        self.__state = True
        print(f"{self.__name} started spinning.")

    def turn_off(self):
        self.__state = False
        print(f"{self.__name} stopped.")

    def status(self):
        return f"{self.__name} is ON" if self.__state else f"{self.__name} is OFF"

# Smart Home Controller
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
        print("\n📡 Device Status:")
        for appliance in self.__appliances:
            print("•", appliance.status())

# CLI menu
def main():
    light = Light()
    fan = Fan()
    controller = SmartHomeController()
    controller.add_appliance(light)
    controller.add_appliance(fan)

    while True:
        print("\n📱 Smart Home Menu")
        print("1. Turn ON all devices")
        print("2. Turn OFF all devices")
        print("3. Show device status")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            controller.activate_all()
        elif choice == "2":
            controller.deactivate_all()
        elif choice == "3":
            controller.show_status()
        elif choice == "4":
            print("👋 Exiting Smart Home System.")
            break
        else:
            print("❌ Invalid option. Try again.")

# Run the CLI
if __name__ == "__main__":
    main()

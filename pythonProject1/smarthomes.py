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
    @property
    def name(self):
        return self.__name

    def __init__(self, name="Light"):
        self.__state = False
        self.__name = name

    def turn_on(self):
        self.__state = True
        print(f"{self.__name} Turned On")

    def turn_off(self):
        self.__state = False
        print(f"{self.__name} Turned Off")

    def status(self):
        return f"{self.__name} is ON" if self.__state else f"{self.__name} is OFF"

class Fan(Appliance):
    @property
    def name(self):
        return self.__name

    def __init__(self, name="Fan"):
        self.__state = False
        self.__name = name

    def turn_on(self):
        self.__state = True
        print(f"{self.__name} Fan Started Spinning ")

    def turn_off(self):
        self.__state = False
        print(f"{self.__name} Fan stopped")

    def status(self):
        return f"{self.__name} is ON" if self.__state else f"{self.__name} is OFF"

class Heater(Appliance):
    @property
    def name(self):
        return self.__name

    def __init__(self, name="Heater"):
        self.__state = False
        self.__name = name

    def turn_on(self):
        self.__state = True
        print(f"{self.__name} Heater is On")

    def turn_off(self):
        self.__state = False
        print(f"{self.__name}  Heater is off")

    def status(self):
        return f"{self.__name} is ON" if self.__state else f"{self.__name} is OFF"

import time

class SmartHomeScheduler:
    def __init__(self):
        self.__appliances = {}

    def add_appliance(self, appliance):
        self.__appliances[appliance.name] = appliance

    def turn_on_all(self):
        for appliance in self.__appliances.values():
            appliance.turn_on()

    def turn_off_all(self):
        for appliance in self.__appliances.values():
            appliance.turn_off()

    def view_status(self):
        for appliance in self.__appliances.values():
            print(appliance.status())

    def schedule(self, appliance_name, action, delay):
        if appliance_name in self.__appliances:
            appliance = self.__appliances[appliance_name]
            print(f"Scheduling {appliance_name} to turn {action.upper()} in {delay} seconds...")
            time.sleep(delay)

            if action.lower() == "on":
                appliance.turn_on()
            elif action.lower() == "off":
                appliance.turn_off()
            else:
                print("Invalid action. Use 'on' or 'off'.")
        else:
            print(f"No appliance found with the name: {appliance_name}")

def main():
    controller = SmartHomeScheduler()

    controller.add_appliance(Light("Kitchen Light"))
    controller.add_appliance(Fan("Bedroom Fan"))
    controller.add_appliance(Heater("Bathroom Heater"))

    while True:
        print("\nSmart Home Schedule Menu:")
        print("1. Add Appliance")
        print("2. Turn ON all devices")
        print("3. Turn OFF all devices")
        print("4. View Status")
        print("5. Schedule Action")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Enter appliance type (Light/Fan/Heater): ").lower()
            custom_name = input("Enter a custom name: ")

            if name == "light":
                appliance = Light(custom_name)
            elif name == "fan":
                appliance = Fan(custom_name)
            elif name == "heater":
                appliance = Heater(custom_name)
            else:
                print("Unknown appliance type.")
                continue

            controller.add_appliance(appliance)
            print(f"✅ {custom_name} added.")

        elif choice == "2":
            controller.turn_on_all()

        elif choice == "3":
            controller.turn_off_all()

        elif choice == "4":
            controller.view_status()

        elif choice == "5":
            appliance_name = input("Enter appliance name to schedule: ")
            action = input("Enter action (on/off): ")
            delay = int(input("Enter delay in seconds: "))
            controller.schedule(appliance_name, action, delay)

        elif choice == "6":
            print("👋 Exiting Smart Home Schedule System.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
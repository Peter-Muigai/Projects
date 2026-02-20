from abc import ABC, abstractmethod


# Abstract class — Abstraction
class Lockdoor(ABC):
    @abstractmethod
    def read_data(self):
        pass


# Concrete implementation
class Pincode(Lockdoor):
    def read_data(self):



class HealthMonitor:
    def __init__(self):
        self.__lock = Pincode()  # Encapsulated sensor

    def check_heart_rate(self):
        heart_rate = self.__lock.read_data()
        print(f"Heart Rate: {heart_rate} bpm")

        if heart_rate < 60:
            print("⚠️ Alert: Heart rate is too low!")
        elif heart_rate > 100:
            print("⚠️ Alert: Heart rate is too high!")
        else:
            print("✅ Heart rate is normal.")


# Test the system
device = HealthMonitor()
device.check_heart_rate()

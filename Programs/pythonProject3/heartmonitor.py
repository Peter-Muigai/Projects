from abc import ABC, abstractmethod


# Abstract class — Abstraction
class Sensor(ABC):
    @abstractmethod
    def read_data(self):
        pass


# Concrete implementation
class HeartRateSensor(Sensor):
    def read_data(self):
        # Simulated reading
        return 120  # beats per minute


class HealthMonitor:
    def __init__(self):
        self.__sensor = HeartRateSensor()  # Encapsulated sensor

    def check_heart_rate(self):
        heart_rate = self.__sensor.read_data()
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

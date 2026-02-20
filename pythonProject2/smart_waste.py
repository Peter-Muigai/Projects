import random
import time

class SmartBin:
    def __init__(self, bin_id, location, capacity=100):
        self.bin_id = bin_id
        self.location = location
        self.capacity = capacity
        self.level = 0

    def fill_bin(self):
        """Simulate waste filling randomly"""
        self.level += random.randint(1, 10)
        if self.level > self.capacity:
            self.level = self.capacity

    def status(self):
        """Return status color"""
        if self.level >= 80:
            return "RED"
        elif self.level >= 50:
            return "YELLOW"
        else:
            return "GREEN"

    def __str__(self):
        return f"Bin {self.bin_id} at {self.location}: {self.level}% full ({self.status()})"


# Create bins using dictionaries + OOP
bins = [
    SmartBin(1, "Market Street"),
    SmartBin(2, "Central Park"),
    SmartBin(3, "Station Road"),
    SmartBin(4, "University Gate")
]

# Simulation loop
for t in range(10):  # 10 simulation cycles
    print(f"\n--- Cycle {t+1} ---")
    for b in bins:
        b.fill_bin()
        print(b)
    time.sleep(1)  # Pause for readability

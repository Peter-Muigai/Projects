import random

class SmartBin:
    def __init__(self, bin_id, location, capacity=100):
        self.bin_id = bin_id
        self.location = location
        self.capacity = capacity
        self.level = 0
        self.alerts = 0  # Count how many times bin overflowed

    def fill_bin(self):
        """Simulate daily waste fill"""
        self.level += random.randint(10, 30)  # each day waste increases
        if self.level > self.capacity:
            self.level = self.capacity
            self.alerts += 1

    def empty_bin(self):
        """Simulate waste collection"""
        self.level = 0

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


# Create bins in the city
bins = [
    SmartBin(1, "Market Street"),
    SmartBin(2, "Central Park"),
    SmartBin(3, "Station Road"),
    SmartBin(4, "University Gate"),
    SmartBin(5, "Hospital Entrance")
]

# Simulate 7 days
for day in range(1, 8):  # 7 days
    print(f"\n===== Day {day} =====")
    for b in bins:
        b.fill_bin()
        print(b)

    # Collect waste if any bin is RED (>=80% full)
    full_bins = [b for b in bins if b.level >= 80]
    if full_bins:
        print("\n🚛 Collection triggered for these bins:")
        for fb in full_bins:
            print(f"  - {fb.location} (was {fb.level}%)")
            fb.empty_bin()

# Summary after 7 days
print("\n===== Weekly Summary =====")
for b in bins:
    print(f"Bin {b.bin_id} at {b.location} overflowed {b.alerts} times.")

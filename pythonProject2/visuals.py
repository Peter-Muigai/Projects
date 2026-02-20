import random
import matplotlib.pyplot as plt

# WasteBin class (OOP)
class WasteBin:
    def __init__(self, bin_id, location, capacity=100):
        self.bin_id = bin_id
        self.location = location
        self.capacity = capacity
        self.fill_level = 0

    def add_waste(self, amount):
        self.fill_level += amount
        if self.fill_level > self.capacity:
            self.fill_level = self.capacity

    def is_full(self):
        return self.fill_level >= 80

    def empty_bin(self):
        self.fill_level = 0


# Initialize bins
bins = {
    1: WasteBin(1, "Market Street"),
    2: WasteBin(2, "City Park"),
    3: WasteBin(3, "Residential Area"),
    4: WasteBin(4, "Shopping Center")
}

# Store history for visualization
history = {bin_id: [] for bin_id in bins}

# Simulate 7 days
for day in range(1, 8):
    print(f"\n📅 Day {day} Report")
    bins_to_collect = []

    for bin_id, bin_obj in bins.items():
        # Add random waste each day
        waste = random.randint(10, 40)
        bin_obj.add_waste(waste)

        # Save history
        history[bin_id].append(bin_obj.fill_level)

        # Check if full
        if bin_obj.is_full():
            bins_to_collect.append(bin_id)

    # Daily summary
    if bins_to_collect:
        print(f"🚛 Collect bins: {bins_to_collect}")
        for b in bins_to_collect:
            bins[b].empty_bin()
    else:
        print("✅ No bins need collection today.")

# Visualization
for bin_id, levels in history.items():
    plt.plot(range(1, 8), levels, marker='o', label=f"Bin {bin_id} ({bins[bin_id].location})")

plt.title("Waste Bin Levels Over 7 Days")
plt.xlabel("Day")
plt.ylabel("Fill Level (%)")
plt.ylim(0, 100)
plt.legend()
plt.grid(True)
plt.show()

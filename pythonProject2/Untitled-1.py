from flask import Flask, jsonify
import random
import threading
import time

app = Flask(__name__)

# Simulated smart bins
bins = [
    {"id": 1, "location": "Market Street", "capacity": 100, "level": 20},
    {"id": 2, "location": "Central Park", "capacity": 100, "level": 40},
    {"id": 3, "location": "Station Road", "capacity": 100, "level": 60},
    {"id": 4, "location": "University Gate", "capacity": 100, "level": 10},
]

# Function to simulate bins filling up
def simulate_bin_fill():
    while True:
        for b in bins:
            # Random increase in waste level
            b["level"] += random.randint(0, 5)
            if b["level"] > b["capacity"]:
                b["level"] = b["capacity"]  # Cap at max
        time.sleep(5)  # Update every 5 seconds

@app.route("/bins", methods=["GET"])
def get_bins():
    """Return current bin data with status."""
    bin_data = []
    for b in bins:
        status = "Green"
        if b["level"] >= 80:
            status = "Red"
        elif b["level"] >= 50:
            status = "Yellow"
        bin_data.append({
            "id": b["id"],
            "location": b["location"],
            "level": b["level"],
            "capacity": b["capacity"],
            "status": status
        })
    return jsonify(bin_data)

if __name__ == "__main__":
    # Run simulation in background thread
    t = threading.Thread(target=simulate_bin_fill, daemon=True)
    t.start()
    app.run(debug=True)

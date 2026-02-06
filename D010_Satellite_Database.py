# Task 1: Initialize the Dictionary
satellite: dict[str, str | int] = {
    "name": "Icarus-1",
    "orbit": 500,
    "status": "Active"
}

# Task 2: Update an existing value
satellite["status"] = "Maintenance"

# Task 3: Add a new key-value pair
satellite["fuel_level"] = 85

# Task 4: Safe Access using .get()
# This avoids a 'KeyError' if the key doesn't exist
launch_date = satellite.get("launch_date", "Unknown")
print(f"Launch Date Check: {launch_date}")

# Task 5: Iteration using .items()
print("--- Satellite Metadata ---")
for key, value in satellite.items():
    print(f"Key: {key} | Value: {value}")

# Task 6: Delete the 'orbit' key
if "orbit" in satellite:
    del satellite["orbit"]

print("\nFinal Update Complete. Orbit data purged.")
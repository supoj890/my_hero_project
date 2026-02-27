# 1. The Input Data
readings: list[float] = [12.5, -99.0, 18.2, 44.1, -99.0, 30.7]

# 2. The Filter: Remove -99.0 (Sensor Errors)
# We cast to list() because filter returns an iterator
cleaned_data = list(filter(lambda x: x != -99.0, readings))

# 3. The Map: Round every value to the nearest whole number
rounded_data = list(map(lambda x: round(x), cleaned_data))

# 4. The Sort: Drone Fleet by Battery (Descending)
fleet = [
    {"id": 3, "bat": 20}, 
    {"id": 1, "bat": 90}, 
    {"id": 2, "bat": 50}
]

# Using sorted() with a lambda key for descending order (reverse=True)
sorted_fleet = sorted(fleet, key=lambda drone: drone["bat"], reverse=True)

# --- Print Results ---
print(f"Original Readings: {readings}")
print(f"Cleaned Data (No Errors): {cleaned_data}")
print(f"Rounded Data: {rounded_data}")
print("\nFleet Status (Sorted by Battery):")
for drone in sorted_fleet:
    print(f"Drone ID: {drone['id']} | Battery: {drone['bat']}%")

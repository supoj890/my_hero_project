# Task 1: Initialize the list with Type Hints
drones: list[str] = ["Raptor", "Ghost", "Shadow"]

# Task 2: Add "Specter" to the end
drones.append("Specter")

# Task 3: Insert "Alpha" at the beginning
drones.insert(0, "Alpha")

# Task 4: Remove "Ghost"
drones.remove("Ghost")

# Task 5: Print total count
print(f"Total Drones in Fleet: {len(drones)}")

# Task 6: Loop and Uppercase
print("Active Drones (UPPERCASE):")
for drone in drones:
    print(f"- {drone.upper()}")

# Task 7: Slicing Challenge (First two drones)
# Slice [0:2] takes index 0 and 1, but stops before 2
first_two = drones[0:2]
print(f"Primary Recon Team: {first_two}")
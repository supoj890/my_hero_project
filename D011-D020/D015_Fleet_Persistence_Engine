import random

# Task 1: Generate Data using a List Comprehension
# One-liner to create a list of 5 drones with random IDs and fuel levels
fleet_data = [{"id": random.randint(1000, 9999), "fuel": random.randint(10, 100)} for _ in range(5)]

# Task 2: Save to Disk
def save_fleet(data: list[dict]):
    """Saves fleet data to a text file in a structured format."""
    with open("fleet_status.txt", "w") as file:
        for drone in data:
            # We use a '|' as a delimiter to make parsing easier later
            file.write(f"ID:{drone['id']}|FUEL:{drone['fuel']}\n")
    print("Fleet data successfully saved to fleet_status.txt")

# Task 3: The Analysis (Load and Filter)
def load_and_filter():
    """Reads the file and identifies drones with low fuel."""
    print("--- Low Fuel Alert Audit ---")
    try:
        with open("fleet_status.txt", "r") as file:
            for line in file:
                # Remove the newline and split by our delimiter '|'
                parts = line.strip().split("|")
                
                # Extract the fuel value (ID:xxxx|FUEL:xx)
                # parts[1] is 'FUEL:xx', so we split again by ':'
                fuel_val = int(parts[1].split(":")[1])
                
                if fuel_val < 30:
                    print(f"[ALERT] {parts[0]} has critically low fuel: {fuel_val}%")
    except FileNotFoundError:
        print("Error: No fleet data file found.")

# --- Execution ---
save_fleet(fleet_data)
load_and_filter()
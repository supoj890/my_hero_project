import json

# Task 1: Prepare the Structured Data
active_fleet = [
    {"name": "Raptor-01", "id": 101, "missions": ["Recon", "Surveillance"], "battery": 85},
    {"name": "Ghost-02", "id": 102, "missions": ["Delivery", "Transport"], "battery": 45},
    {"name": "Shadow-03", "id": 103, "missions": ["Night-Ops"], "battery": 20}
]

# Task 2: Save as JSON (Pretty Printed)
with open("fleet_db.json", "w") as f:
    # indent=4 makes the file look organized in VS Code
    json.dump(active_fleet, f, indent=4)

# Task 3: The "Live" Update Function
def update_battery(target_name: str, new_level: int) -> None:
    """Loads, updates, and saves the JSON fleet database."""
    try:
        # Load Phase
        with open("fleet_db.json", "r") as f:
            fleet_data = json.load(f)
        
        # Update Phase
        updated = False
        for drone in fleet_data:
            if drone["name"] == target_name:
                drone["battery"] = new_level
                updated = True
                break
        
        # Save Phase (only if we found the drone)
        if updated:
            with open("fleet_db.json", "w") as f:
                json.dump(fleet_data, f, indent=4)
            print(f"Successfully updated {target_name} to {new_level}% battery.")
        else:
            print(f"Drone '{target_name}' not found in database.")
            
    except FileNotFoundError:
        print("Error: fleet_db.json does not exist.")

# --- Execution ---
update_battery("Ghost-02", 100)
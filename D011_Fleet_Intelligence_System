# Task 1 & 2: Initialize the fleet and define drones
fleet: list[dict[str, str | int]] = []

# Task 3: Append drones to the fleet list
fleet.append({"id": 101, "model": "Predator", "battery": 95})
fleet.append({"id": 102, "model": "GlobalHawk", "battery": 40})
fleet.append({"id": 103, "model": "Reaper", "battery": 15})

# Task 4: The Analysis Loop
print("--- Fleet Intelligence Report ---")
for drone in fleet:
    # Extract data from the dictionary inside the list
    d_id = drone["id"]
    d_model = drone["model"]
    d_battery = drone["battery"]
    
    if d_battery < 20:
        print(f"[ALERT] Drone {d_id} ({d_model}) needs immediate charging!")
    else:
        print(f"Drone {d_id} is operational at {d_battery}%.")

# Task 5: Targeted Update
# Index 1 is the second drone (GlobalHawk)
fleet[1]["battery"] = 100

print(f"\nUpdate: Drone {fleet[1]['id']} battery restored to {fleet[1]['battery']}%")
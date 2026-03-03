import json
from typing import Any

# 1. The Inputs
ids: list[int] = [101, 102, 103, 104, 105]
status: list[str] = ["Active", "Active", "Down", "Active", "Maintenance"]
battery: list[int] = [90, 85, 0, 45, 12]

def process_fleet() -> list[dict[str, Any]]:
    # Step 2 & 3: Zip and List Comprehension with Validation
    fleet_data = []
    for i, s, b in zip(ids, status, battery):
        # Validation Guardrail
        if b > 100 or b < 0:
            raise ValueError(f"Invalid battery level detected for Drone {i}: {b}%")
        
        fleet_data.append({"id": i, "status": s, "battery": b})
    
    return fleet_data

# Execute the pipeline
try:
    full_fleet = process_fleet()

    # Step 4: The Filter (Status is "Down" OR battery < 15)
    urgent_repairs = list(filter(
        lambda drone: drone["status"] == "Down" or drone["battery"] < 15, 
        full_fleet
    ))

    # Step 5: The Persistence (Save to JSON)
    with open("audit_report.json", "w") as f:
        json.dump(urgent_repairs, f, indent=4)

    print(f"Audit Complete. {len(urgent_repairs)} drones flagged for urgent repair.")
    print("Report saved to audit_report.json")

except ValueError as e:
    print(f"Audit Aborted: {e}")
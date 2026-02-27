def refuel_drone(current_fuel: int, added_fuel: int) -> int:
    """
    Enforces safety protocols for drone refueling.
    Raises ValueError if safety limits are breached.
    """
    # Validation 1: Check for negative fuel input
    if added_fuel < 0:
        raise ValueError("Cannot add negative fuel.")

    # Validation 2: Check for tank capacity (Max 100)
    if current_fuel + added_fuel > 100:
        raise ValueError("Fuel tank overflow detected.")

    return current_fuel + added_fuel

# --- Main Execution ---
starting_fuel = 30
shipments = [20, 50, -10, 100]

print(f"Initial Fuel Level: {starting_fuel}%\n")

for shipment in shipments:
    try:
        # Attempt the refueling process
        new_fuel = refuel_drone(starting_fuel, shipment)
        print(f"Refuel Success: Added {shipment} units. New Level: {new_fuel}%")
        # Update starting_fuel if you want the tank to accumulate (optional)
        # starting_fuel = new_fuel 
    except ValueError as e:
        # Catch and report the specific safety breach
        print(f"Refuel Failed: {e}")

print("\nSafety Protocol Check Complete.")
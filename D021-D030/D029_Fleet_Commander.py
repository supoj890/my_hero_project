class Drone:
    """The base unit of our fleet."""
    def __init__(self, callsign: str, battery: int):
        self.callsign = callsign
        self.battery = battery

    def __repr__(self):
        return f"{self.callsign} ({self.battery}%)"

class FleetManager:
    """The central command hub for multiple drone units."""
    def __init__(self):
        # Initializing the fleet as an empty list
        self.drones: list[Drone] = []

    def add_drone(self, drone: Drone) -> None:
        """Enrolls a new drone into the management system."""
        self.drones.append(drone)
        print(f"Registered: {drone.callsign}")

    def emergency_land_all(self) -> None:
        """Executes a mandatory landing sequence for every unit."""
        print("\n--- EMERGENCY PROTOCOL ACTIVATED ---")
        for drone in self.drones:
            print(f"Emergency landing {drone.callsign}!")

    def get_ready_drones(self) -> list[Drone]:
        """Filters the fleet for units with sufficient power (> 25%)."""
        return [d for d in self.drones if d.battery > 25]

# --- The Test ---

# 1. Initialize the Commander
manager = FleetManager()

# 2. Add 4 drones with varying battery levels
manager.add_drone(Drone("Falcon-1", 100))
manager.add_drone(Drone("Falcon-2", 50))
manager.add_drone(Drone("Falcon-3", 10))  # Low battery
manager.add_drone(Drone("Falcon-4", 80))

# 3. Identify Ready Drones
ready_units = manager.get_ready_drones()
print(f"\nUnits Ready for Deployment (Battery > 25%):")
for unit in ready_units:
    print(f"- {unit.callsign} [Status: OK]")

# 4. Trigger Global Emergency
manager.emergency_land_all()
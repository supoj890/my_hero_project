class Drone:
    def __init__(self, callsign: str):
        self.callsign = callsign
    
    def __repr__(self):
        return f"Drone('{self.callsign}')"

class Fleet:
    def __init__(self):
        # Initialize the storage for our drone objects
        self.drones = []

    def add(self, drone: Drone) -> None:
        """Adds a drone instance to the fleet."""
        self.drones.append(drone)

    def __len__(self) -> int:
        """Allows use of len(my_fleet)."""
        return len(self.drones)

    def __str__(self) -> str:
        """Allows use of print(my_fleet)."""
        return f"Fleet containing {len(self.drones)} drones."

    def __getitem__(self, index: int) -> Drone:
        """Allows use of my_fleet[index] (Indexing)."""
        return self.drones[index]

# --- The Test ---

# 1. Setup the fleet and add 3 drones
my_fleet = Fleet()
my_fleet.add(Drone("Raptor-01"))
my_fleet.add(Drone("Ghost-02"))
my_fleet.add(Drone("Omega-03"))

# 2. Test __len__
print(f"Fleet Size (via len): {len(my_fleet)}")

# 3. Test __str__
print(f"Fleet Summary: {my_fleet}")

# 4. Test __getitem__
print(f"Accessing index 0: {my_fleet[0]}")
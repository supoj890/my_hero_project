class Drone:
    """
    The base prototype for all fleet units.
    Encapsulates callsign, model, and power management.
    """
    
    def __init__(self, callsign: str, model: str):
        # The Constructor: Setting up the initial state
        self.callsign = callsign
        self.model = model
        self.battery = 100  # Default starting charge

    def fly(self, distance: int) -> None:
        """
        Reduces battery based on flight distance (Integer division // 2).
        """
        drain = distance // 2
        self.battery -= drain
        
        # Guardrail to ensure battery doesn't go negative
        if self.battery < 0:
            self.battery = 0
            
        print(f"{self.callsign} is airborne. Battery now: {self.battery}%")

    def get_status(self) -> str:
        """
        Returns a formatted string of the drone's current specs.
        """
        return f"Drone: {self.callsign} | Model: {self.model} | Battery: {self.battery}%"

# --- Execution ---

# 1. Create two separate objects (instances of the class)
drone_1 = Drone("Raptor", "v4")
drone_2 = Drone("Ghost", "vX")

# 2. Make drone_1 fly 20 units
drone_1.fly(20)

# 3. Print the status of both drones
print("\n--- Fleet Status Report ---")
print(drone_1.get_status())
print(drone_2.get_status())
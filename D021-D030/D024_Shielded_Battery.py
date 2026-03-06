class ShieldedDrone:
    def __init__(self):
        # Private attribute (double underscore prefix)
        self.__battery = 100

    @property
    def battery(self) -> int:
        """The Getter: Provides read access to the private battery."""
        return self.__battery

    @battery.setter
    def battery(self, value: int) -> None:
        """The Setter: Acts as a guardrail for all battery changes."""
        if value > 100:
            print(f"Warning: {value}% exceeds capacity. Capping at 100%.")
            self.__battery = 100
        elif value < 0:
            print(f"Warning: {value}% is below zero. Setting to 0%.")
            self.__battery = 0
        else:
            self.__battery = value

# --- The Test ---

drone = ShieldedDrone()

# Attempt 1: Overflow
print("Attempting to set battery to 150...")
drone.battery = 150
print(f"Current Battery: {drone.battery}%")

print("-" * 30)

# Attempt 2: Underflow
print("Attempting to set battery to -20...")
drone.battery = -20
print(f"Current Battery: {drone.battery}%")

print("-" * 30)

# Attempt 3: Valid change
print("Attempting to set battery to 75...")
drone.battery = 75
print(f"Current Battery: {drone.battery}%")
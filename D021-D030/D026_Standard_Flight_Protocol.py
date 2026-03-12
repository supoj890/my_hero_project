from abc import ABC, abstractmethod

# 1. Define the Abstract Class (The Contract)
class BaseDrone(ABC):
    
    @abstractmethod
    def takeoff(self):
        """Must be implemented by any drone subclass."""
        pass

    @abstractmethod
    def land(self):
        """Must be implemented by any drone subclass."""
        pass

# 2. Define the Concrete Class (The Implementation)
class CourierDrone(BaseDrone):
    def __init__(self, callsign: str):
        self.callsign = callsign

    def takeoff(self):
        print(f"[Protocol] {self.callsign}: Rotors spinning. Clearing the pad.")

    def land(self):
        print(f"[Protocol] {self.callsign}: Descent sequence complete. Powering down.")

# --- The Test ---

# This will work because CourierDrone fulfilled the contract
drone = CourierDrone("Swift-Deliver-1")
drone.takeoff()
drone.land()

# This WILL FAIL (Uncomment to test the error)
# try:
#     ghost_drone = BaseDrone()
# except TypeError as e:
#     print(f"\nCaught Expected Error: {e}")
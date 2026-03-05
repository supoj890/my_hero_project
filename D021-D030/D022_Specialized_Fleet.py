class Drone:
    """The Base Parent Class"""
    def __init__(self, callsign: str, model: str):
        self.callsign = callsign
        self.model = model
        self.battery = 100

    def fly(self, distance: int) -> None:
        drain = distance // 2
        self.battery -= drain
        print(f"[Standard] {self.callsign} flew {distance} units. Battery: {self.battery}%")

# 1. Define the ReconDrone (Inheritance)
class ReconDrone(Drone):
    def __init__(self, callsign: str, model: str, camera_type: str):
        # Use super() to initialize parent attributes
        super().__init__(callsign, model)
        self.camera_type = camera_type

    # Override the fly method for better efficiency
    def fly(self, distance: int) -> None:
        drain = distance // 4  # Recon is 2x more efficient
        self.battery -= drain
        print(f"[Recon] {self.callsign} (Cam: {self.camera_type}) flew {distance} units. Battery: {self.battery}%")

# 2. Define the CargoDrone (Inheritance)
class CargoDrone(Drone):
    def __init__(self, callsign: str, model: str, max_weight: int):
        super().__init__(callsign, model)
        self.max_weight = max_weight

    # Override fly logic (Cargo is heavy!)
    def fly(self, distance: int) -> None:
        drain = distance  # Cargo drains 1:1
        self.battery -= drain
        print(f"[Cargo] {self.callsign} (Max Load: {self.max_weight}kg) flew {distance} units. Battery: {self.battery}%")

# 3. The Fleet Test (Polymorphism in action)
my_fleet = [
    Drone("Alpha-1", "v1"),
    ReconDrone("Ghost-9", "Stealth-X", "Infrared"),
    CargoDrone("Atlas-Heavy", "Hauler-4", 500)
]

print("--- Launching Fleet for 40-unit Flight ---")
for drone in my_fleet:
    drone.fly(40)
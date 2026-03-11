import json

class FleetDrone:
    # Class Variable: Shared by all instances of FleetDrone
    total_drones = 0

    def __init__(self, callsign: str, model: str):
        self.callsign = callsign
        self.model = model
        # Increment the global fleet counter every time a drone is born
        FleetDrone.total_drones += 1

    @classmethod
    def from_json(cls, json_data: str):
        """
        Factory Method: Creates a FleetDrone instance from a JSON string.
        """
        data = json.loads(json_data)
        # 'cls' refers to the FleetDrone class itself
        return cls(data["callsign"], data["model"])

# --- The Test ---

# 1. Create two drones the traditional way
drone_1 = FleetDrone("Alpha", "v1")
drone_2 = FleetDrone("Beta", "v2")

# 2. Create a third drone using the JSON Factory
json_input = '{"callsign": "Omega", "model": "v9"}'
drone_3 = FleetDrone.from_json(json_input)

# 3. Verify the factory count
print(f"Drone 3 created: {drone_3.callsign} ({drone_3.model})")
print(f"Total Drones in Fleet: {FleetDrone.total_drones}")
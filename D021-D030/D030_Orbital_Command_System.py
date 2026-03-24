import json
from abc import ABC, abstractmethod

# --- 1. The Base: Drone with Encapsulation ---
class Drone:
    def __init__(self, callsign: str, model: str):
        self.callsign = callsign
        self.model = model
        self.__battery = 100  # Private attribute

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        if value > 100: self.__battery = 100
        elif value < 0: self.__battery = 0
        else: self.__battery = value

    def fly(self, distance: int):
        drain = distance // 2
        self.battery -= drain
        return self.battery > 0

# --- 2. The Child: Specialized Heavy Lift ---
class HeavyLiftDrone(Drone):
    def __init__(self, callsign: str, model: str, cargo_capacity: int):
        super().__init__(callsign, model)
        self.cargo_capacity = cargo_capacity

    def fly(self, distance: int):
        # Heavy lift is less efficient due to weight
        drain = distance  # 1:1 drain ratio
        self.battery -= drain
        return self.battery > 0

# --- 3. The Target and Mission Logic ---
class Target:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x, self.y = x, y

class Mission:
    def __init__(self, drone: Drone, target: Target):
        self.drone = drone
        self.target = target
        self.status = "Pending"

    def run(self):
        distance = abs(self.target.x) + abs(self.target.y)
        success = self.drone.fly(distance)
        self.status = "Success" if success else "Failure"
        return self.status

# --- 4. The Manager: Orbital Command ---
class OrbitalCommand:
    def __init__(self):
        self.missions: list[Mission] = []

    def add_mission(self, mission: Mission):
        self.missions.append(mission)

    def execute_all(self):
        print(f"--- Executing {len(self.missions)} Orbital Missions ---")
        for m in self.missions:
            result = m.run()
            print(f"Drone {m.drone.callsign} -> {m.target.name}: {result}")

    def save_history(self, filename: str):
        history = [
            {
                "drone": m.drone.callsign,
                "target": m.target.name,
                "result": m.status,
                "remaining_battery": m.drone.battery
            } for m in self.missions
        ]
        with open(filename, 'w') as f:
            json.dump(history, f, indent=4)
        print(f"\nMission history saved to {filename}")

# --- The Test ---
# 1. Setup
atlas = HeavyLiftDrone("Atlas-01", "H-Class", cargo_capacity=500)
mars_base = Target("Mars North Pole", x=30, y=40)

# 2. Command Center
command = OrbitalCommand()
command.add_mission(Mission(atlas, mars_base))

# 3. Execution & Persistence
command.execute_all()
command.save_history("orbital_log.json")
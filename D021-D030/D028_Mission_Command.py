class Drone:
    """A simple version of our previous Drone class."""
    def __init__(self, callsign: str, battery: int = 100):
        self.callsign = callsign
        self.battery = battery

    def fly(self, distance: int) -> None:
        drain = distance // 2
        self.battery -= drain
        print(f"{self.callsign} flying {distance} units... Battery remaining: {self.battery}%")

class Target:
    """Represents the objective coordinates."""
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y

class Mission:
    """The 'Controller' class that orchestrates the Drone and Target."""
    def __init__(self, drone: Drone, target: Target):
        self.drone = drone
        self.target = target

    def calculate_distance(self) -> int:
        """Simplified Manhattan distance: |x| + |y|"""
        return abs(self.target.x) + abs(self.target.y)

    def start(self) -> None:
        """Executes the flight and checks for success."""
        distance = self.calculate_distance()
        print(f"Mission Start: Heading to {self.target.name} ({distance} units away)")
        
        # Command the drone object to act
        self.drone.fly(distance)

        # Evaluate the state of the drone object after the action
        if self.drone.battery > 0:
            print("MISSION SUCCESS: Objective reached.")
        else:
            print("MISSION FAILED: Power lost mid-flight.")

# --- The Test ---

# 1. Setup the participants
raptor = Drone("Raptor-01", battery=100)
hq_target = Target("Command Center", x=40, y=20)

# 2. Initialize and run the mission
active_mission = Mission(raptor, hq_target)
active_mission.start()
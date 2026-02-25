# Task 1: Import the Standard Library toolkits
import math
import random
import datetime

# Task 2: The Math Task
calculation = math.sqrt(225)
print(f"Trajectory Calculation (Square Root of 225): {calculation}")

# Task 3: The Random Task
landing_sites: list[str] = ["Crater-A", "Plain-B", "Ridge-C"]
selected_site = random.choice(landing_sites)
print(f"Target Site: {selected_site}")

# Task 4: The Time Task
now = datetime.datetime.now()
# strftime formats the time into a human-readable string
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Landing Timestamp: {formatted_time}")

# Task 5: Integration (Append to Log)
with open("mission_log.txt", "a") as file:
    log_entry = f"[{formatted_time}] LANDING SEQUENCE INITIATED: {selected_site}\n"
    file.write(log_entry)

print("Mission log updated successfully.")
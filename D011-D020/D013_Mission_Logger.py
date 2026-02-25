# Task 1: Define initial data
logs: list[str] = ["Engines Started", "Fuel Level: 95%", "Oxygen Check: OK"]

# Task 2: The Write Phase ("w" overwrites any existing content)
with open("mission_log.txt", "w") as file:
    for entry in logs:
        # We add \n (newline) to ensure each log is on its own line
        file.write(entry + "\n")

# Task 3: The Append Phase ("a" adds to the bottom of the file)
with open("mission_log.txt", "a") as file:
    file.write("Liftoff Confirmed\n")

# Task 4: The Read Phase ("r" allows us to see the content)
with open("mission_log.txt", "r") as file:
    final_report = file.read()

print("--- Spacecraft Black Box Report ---")
print(final_report)
# Task 1: Initialize the starting temperature
current_temp: int = 60

# Task 2: The While Loop (Runs as long as the condition is True)
while current_temp <= 100:
    print(f"System Check: {current_temp}°C")
    
    # Task 3: Conditional check inside the loop
    if current_temp == 85:
        print(f"WARNING: Fan engaged at {current_temp}°C")
    
    # Task 4: Increment (Essential to avoid an infinite loop!)
    current_temp += 5

# Task 5: Post-loop critical message
print(f"CRITICAL: System Shutdown at {current_temp}°C")

print("-" * 20) # Visual separator

# The "For" Twist: Reboot sequence
# range(1, 4) starts at 1 and stops BEFORE 4 (1, 2, 3)
for i in range(1, 4):
    print(f"Rebooting attempt {i}...")
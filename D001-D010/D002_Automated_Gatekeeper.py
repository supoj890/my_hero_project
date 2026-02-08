# Task 1: Define variables with Type Hints
has_badge: bool = True
clearance_level: int = 6
is_emergency: bool = False

# Challenge: The Guard Clause Logic
# We handle the most critical condition first and 'exit' the logic early.


if is_emergency:
    print(f"EMERGENCY: ALL GATES OPEN.")
    # In a real app, we might use 'return' or 'exit()' here
    # but for a script, we use 'if/elif/else' to keep it clean.
elif not has_badge:
    print(f"Access Denied: No Badge Detected.")
elif clearance_level >= 5:
    print(f"Access Granted: High Security Zone.")
else:
    print(f"Access Granted: General Zone.")
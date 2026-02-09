# Task 1: Tuples (Immutability)
hq_location: tuple[float, float] = (37.7749, -122.4194)

# hq_location[0] = 38.0  # ERROR: Tuples cannot be changed after creation
print(f"HQ Location (Fixed): {hq_location}")

# Task 2 & 3: Lists vs. Sets (Uniqueness)
raw_logs: list[str] = ["A1", "B2", "A1", "C3", "B2", "D4", "A1"]
unique_visitors: set[str] = set(raw_logs)

# Task 4: Audit Check
print(f"Total entries in log: {len(raw_logs)}")
print(f"Unique visitors identified: {len(unique_visitors)}")

# Task 5: Adding to a Set
unique_visitors.add("E5")

# Task 6 & 7: Set Intersection (Forbidden Zone Check)
restricted_area: set[str] = {"B2", "F6"}

# Find overlapping badge IDs
intruders = unique_visitors & restricted_area

print(f"Restricted Area Intrusion Detected: {intruders}")
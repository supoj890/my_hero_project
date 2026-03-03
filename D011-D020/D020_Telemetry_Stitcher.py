# 1. Input Lists (The raw sensor feeds)
timestamps: list[str] = ["12:00", "12:01", "12:02"]
altitudes: list[int] = [150, 165, 180]
velocities: list[float] = [45.2, 47.1, 46.8]

# --- Method A: The Readable Loop ---
telemetry_data = []

# Using zip() to iterate through all three simultaneously
for time, alt, vel in zip(timestamps, altitudes, velocities):
    snapshot = {
        "timestamp": time,
        "altitude": alt,
        "velocity": vel
    }
    telemetry_data.append(snapshot)

# --- Method B: The Advanced "One-Liner" (List Comprehension) ---
# This achieves Task 2 & 3 in a single, Pythonic stroke
telemetry_data_compact = [
    {"timestamp": t, "altitude": a, "velocity": v} 
    for t, a, v in zip(timestamps, altitudes, velocities)
]

# Final Print
print("--- Stitched Telemetry Data ---")
for entry in telemetry_data_compact:
    print(entry)
     
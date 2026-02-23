from typing import Any

def master_logger(level: str, *events: Any, **metadata: Any) -> None:
    """
    A universal logging wrapper that handles a variable number of
    status updates and metadata tags.
    """
    # 1. Print the level in uppercase
    print(f"--- [{level.upper()}] ---")

    # 2. Loop through the *events tuple (positional arguments)
    for event in events:
        print(f"EVENT: {event}")

    # 3. Loop through the **metadata dictionary (keyword arguments)
    for key, value in metadata.items():
        # Formatting key to look like 'Key: Value'
        print(f"{key.replace('_', ' ').title()}: {value}")

# The "Call"
master_logger(
    "DEBUG", 
    "Engine Sync", 
    "Fuel Flow OK", 
    drone_id=101, 
    sector="Gama-9"
)
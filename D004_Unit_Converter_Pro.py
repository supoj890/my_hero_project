# Task 1: Define the Conversion Function
def celsius_to_fahrenheit(temp_c: float) -> float:
    """Converts Celsius to Fahrenheit."""
    # Formula: F = (C * 9/5) + 32
    return (temp_c * 9/5) + 32

# Task 2: Define the Safety Check Function
def check_safety(temp_f: float) -> str:
    """Returns safety status based on Fahrenheit temperature."""
    if temp_f < 212.0:
        return "SAFE"
    else:
        return "DANGER"

# --- Execution Block ---
my_celsius: float = 100.0

# Call first function
result_f = celsius_to_fahrenheit(my_celsius)

# Call second function and print result
status = check_safety(result_f)

print(f"Celsius: {my_celsius}°C")
print(f"Fahrenheit: {result_f}°F")
print(f"Status: {status}")
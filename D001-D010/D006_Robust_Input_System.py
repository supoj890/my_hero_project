def get_user_age() -> int | None:
    """Gets age from user and handles non-numeric input."""
    user_input = input("Enter your age: ")
    
    try:
        # Tries to convert string to integer
        age = int(user_input)
        return age
    except ValueError:
        # Runs ONLY if the conversion above fails
        print("Invalid input. Please enter a number.")
        return None
    finally:
        # Runs EVERY time, whether there was an error or not
        print("Age check attempt complete.")

# --- Main Logic ---
age_result = get_user_age()

# Check if we got a valid number back
if age_result is not None:
    if age_result >= 18:
        print("Access Granted: Welcome to the system.")
    else:
        print("Access Denied: You must be 18 or older.")
else:
    print("System Error: No valid age provided.")
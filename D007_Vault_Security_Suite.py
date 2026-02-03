# Task 1: The Validation Logic (Unit-style function)
def validate_code(attempt: str) -> bool:
    """Tries to convert input and check against the secret code."""
    secret_code: int = 1337
    
    try:
        # We wrap only the risky conversion in the try block
        if int(attempt) == secret_code:
            return True
        else:
            return False
    except ValueError:
        # If they typed letters, it's a False attempt, not a crash
        print("Error: Numeric code required.")
        return False

# Task 2: The Main Controller
def run_vault() -> None:
    """Manages the user attempts and security state."""
    max_attempts: int = 3
    
    print("--- DIGITAL VAULT SYSTEM ACTIVE ---")
    
    while max_attempts > 0:
        user_input = input(f"Enter Vault Code ({max_attempts} attempts left): ")
        
        if validate_code(user_input):
            print("VAULT UNLOCKED: Welcome, Hero.")
            break # Exit the loop immediately
        else:
            max_attempts -= 1
            if max_attempts > 0:
                print("Access Denied. Recalibrating security...")
    
    # After the loop, check if they failed all attempts
    if max_attempts == 0:
        print("ALARM TRIGGERED: SYSTEM LOCKDOWN.")

# --- Start the program ---
run_vault()
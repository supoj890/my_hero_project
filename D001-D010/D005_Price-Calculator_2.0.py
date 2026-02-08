# Task 1: The Scope Challenge (Global Variable)
currency: str = "USD"

# Task 2: Function with Default Parameters
def calculate_total(price: float, discount: float = 0.0, tax_rate: float = 0.07) -> float:
    """Calculates final price after discount and tax."""
    
    # Logic: Subtract discount first
    discounted_price = price - discount
    
    # Apply tax
    final_total = discounted_price + (discounted_price * tax_rate)
    
    # Rounding to 2 decimal places
    result = round(final_total, 2)
    
    # Using the Global variable inside the function
    print(f"Checkout Summary [{currency}]: {result}")
    
    return result

# --- Execution ---
print("Test 1 (Standard):")
calculate_total(100.0)  # Uses default discount (0.0) and tax (0.07)

print("\nTest 2 (With Discount):")
calculate_total(100.0, 20.0)  # Uses custom discount but default tax
# Task 1: Declare variables with Type Hints (Best practice for AI and readability)
username: str = "Hero_Supoj"
access_code: int = 4221
is_admin: bool = True

# Task 2 & 3: Memory Address Inspection
# Python objects live in memory. The id() function shows you where.
print(f"Initial access_code ID: {id(access_code)}")

access_code = 9999
print(f"Updated access_code ID: {id(access_code)}")
# HERO NOTE: Notice the IDs are different! Integers are 'immutable' in Python.
# You didn't change the number; you created a new number and moved the label.

# Task 4: Simple Calculation
security_level = access_code * 2

# Task 5: The Formatted String (f-string)
# f-strings are the industry standard for combining variables and text.
print(f"User {username} has security level {security_level}. Admin Status: {is_admin}")

# Extra Credit: The Guardrail Test
# Uncomment the line below to see why Python is 'Strongly Typed'
# print(username + access_code)
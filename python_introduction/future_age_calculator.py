# Define the assumed current year and the target year
CURRENT_YEAR = 2023
TARGET_YEAR = 2050

# Calculate the difference in years
YEARS_TO_ADD = TARGET_YEAR - CURRENT_YEAR  # 2050 - 2023 = 27

# Prompt the user to input their current age and convert the input string to an integer
# We assume the user inputs a valid integer as per the instructions
try:
    current_age_input = input("How old are you? ")
    current_age = int(current_age_input)

    # Calculate the user's age in the target year (2050)
    future_age = current_age + YEARS_TO_ADD

    # Print the result in the specified format
    print(f"In {TARGET_YEAR}, you will be {future_age} years old.")

except ValueError:
    # Basic error handling in case the user enters non-integer input
    print("Invalid input. Please enter a whole number for your age.")

# Example Interaction:
# If input is 30, output is:
# In 2050, you will be 57 years old.
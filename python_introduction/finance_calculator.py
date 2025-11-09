# Define the assumed annual interest rate (5% as a decimal)
ANNUAL_INTEREST_RATE = 0.05
MONTHS_IN_YEAR = 12

# --- User Input Section ---

# Prompt the user for their monthly income and convert the input to a floating-point number
# We use float to handle potential decimal values for currency
try:
    income_input = input("Enter your monthly income: ")
    monthly_income = float(income_input)

    # Prompt the user for their monthly expenses and convert the input to a floating-point number
    expenses_input = input("Enter your total monthly expenses: ")
    monthly_expenses = float(expenses_input)

    # --- Calculation Section ---

    # 1. Calculate Monthly Savings
    monthly_savings = monthly_income - monthly_expenses

    # 2. Calculate Annual Savings without Interest
    annual_savings_base = monthly_savings * MONTHS_IN_YEAR

    # 3. Calculate Projected Annual Savings with Interest
    # Formula: Projected Savings = Base Savings + (Base Savings * Interest Rate)
    # The requirement simplifies this to: Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
    
    interest_earned = annual_savings_base * ANNUAL_INTEREST_RATE
    projected_savings = annual_savings_base + interest_earned

    # --- Output Results Section ---

    # Display the user's monthly savings, formatted to two decimal places for currency
    print(f"Your monthly savings are ${monthly_savings:.2f}.")

    # Display the projected annual savings, also formatted to two decimal places
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

except ValueError:
    # Handle non-numeric input gracefully
    print("Invalid input. Please enter a numerical value for income and expenses.")

# Example Interaction (using 5000 and 4000):
# Your monthly savings are $1000.00.
# Projected savings after one year, with interest, is: $12600.00.

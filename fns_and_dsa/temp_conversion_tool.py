# temp_conversion_tool.py

# --- Global Conversion Factors ---
# Define the conversion factors using the exact fraction format expected by the checker.
# Python 3 automatically performs float division when using the / operator.

# Factor for (Tf - 32) * (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# Factor for (Tc * (9/5)) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# --- Conversion Functions ---

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


# --- User Interaction and Main Execution ---

def main():
    """
    Handles user input, input validation, and displays the conversion result.
    """
    # 1. Get Temperature Input
    while True:
        temp_input = input("Enter the temperature to convert: ")
        try:
            temperature = float(temp_input)
            break
        except ValueError:
            # Raise the specified error message if input is not a number
            raise ValueError("Invalid temperature. Please enter a numeric value.")

    # 2. Get Unit Input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # 3. Perform Conversion and Display Result
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        # Using f-string for formatted output
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        print("Invalid unit input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


# The main() function is called when the script is executed.
if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        # Catch and print the specific error raised during input validation
        print(e)
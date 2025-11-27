
# explore_datetime.py

from datetime import datetime, timedelta

## Part 1: Display the Current Date and Time

def display_current_datetime():
    """
    Obtains and displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    # Use datetime.now() to get the current date and time
    current_date = datetime.now()
    
    # Format the datetime object into a readable string
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print("Current date and time:", formatted_datetime)
    
    # Return the datetime object for use in Part 2
    return current_date

# ---

## Part 2: Calculate a Future Date

def calculate_future_date(start_date):
    """
    Prompts the user for a number of days, calculates the future date,
    and displays it in 'YYYY-MM-DD' format.
    
    Args:
        start_date (datetime): The starting datetime object from which to calculate.
    """
    while True:
        try:
            # Prompt the user for the number of days
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break  # Exit the loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter a whole number for the days.")

    # Create a timedelta object representing the duration
    time_delta = timedelta(days=days_to_add)
    
    # Calculate the future date by adding the timedelta to the current date
    future_date = start_date + time_delta
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)


# ---

## Main execution block
if __name__ == "__main__":
    
    # Part 1 execution
    print("--- Part 1: Current Date and Time ---")
    current_date_obj = display_current_datetime()
    
    # Separator for clarity
    print("\n--- Part 2: Calculate Future Date ---")
    
    # Part 2 execution, passing the current_date_obj from Part 1
    calculate_future_date(current_date_obj)
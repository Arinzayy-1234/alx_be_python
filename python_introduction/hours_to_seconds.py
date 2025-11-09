# Define the number of hours to be converted
hours = 2

# Calculate the number of seconds.
# There are 60 minutes in an hour and 60 seconds in a minute (60 * 60 = 3600 seconds/hour)
SECONDS_PER_HOUR = 3600
seconds = hours * 3600  

# Print the result in the specified format
print(f"{hours} hour(s) is {seconds} seconds")

# Expected Output:
# 2 hour(s) is 7200 seconds.
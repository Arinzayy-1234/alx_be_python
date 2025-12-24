# weather_advice.py

# Prompt the user for input using the exact string required
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Conditional logic to provide recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    # Handling unexpected input
    print("Sorry, I don't have recommendations for this weather.")
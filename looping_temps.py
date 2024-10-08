# TODO: Define a list of temperatures
temperatures = [12, 34, 34, 30, 32, 21, 38]
# TODO: Write a loop to go through each temperature in the list
for temp in temperatures:
    if temp > 30:
        print("It's really hot.")
        break
    # TODO: Add an 'if' statement to check if the temperature is over a really hot threshold
        # TODO: Print a message for being really hot and then exit the loop
    # TODO: Add an 'elif' condition before the general temperature message to check if it's too cold
    elif temp<20:
        print("It's too cold")
        continue
        # TODO: For temperatures that are too cold, print a specific message and skip to the next one
    # TODO: Print a message saying the temperature is nice for all other cases
    print("Nice weather")
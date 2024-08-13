def heating_cooling(actual_temp, desired_temp):
    if actual_temp < desired_temp - 5:
        print("Run heat")
    elif actual_temp > desired_temp + 5:
        print("Run A/C")
    else:
        print("Standby")

# Test the function with various parameters
print("Testing with different parameters:")
heating_cooling(60, 68)   # Expected: Run heat (60 is more than 5 degrees below 68)
heating_cooling(75, 68)   # Expected: Run A/C (75 is more than 5 degrees above 68)
heating_cooling(65, 68)   # Expected: Standby (65 is within 5 degrees of 68)
heating_cooling(70, 70)   # Expected: Standby (70 is within 5 degrees of 70)
heating_cooling(72, 67)   # Expected: Run A/C (72 is more than 5 degrees above 67)

# Prompt user for actual and desired temperatures
print("\nPlease enter your actual and desired temperatures.")
actual_temp = float(input("Enter the actual temperature: "))
desired_temp = float(input("Enter the desired temperature: "))

# Call the function with user input
heating_cooling(actual_temp, desired_temp)

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    # Use global conversion factor to convert F to C
    # Formula: (F - 32) * (5/9)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    # Use global conversion factor to convert C to F
    # Formula: (C * 9/5) + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
def get_temperature_input():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        return temperature
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_unit_input():
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit not in ['C', 'F']:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    return unit


def main():
    try:
        # Get temperature input from user
        temperature = get_temperature_input()
        
        # Get unit input from user
        unit = get_unit_input()
        
        # Perform conversion based on the unit
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
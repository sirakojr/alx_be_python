# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature (e.g., 100C or 212F): ").strip()
        if temp_input[-1].upper() == "C":
            celsius = float(temp_input[:-1])
            print(f"{celsius}°C is {convert_to_fahrenheit(celsius):.2f}°F")
        elif temp_input[-1].upper() == "F":
            fahrenheit = float(temp_input[:-1])
            print(f"{fahrenheit}°F is {convert_to_celsius(fahrenheit):.2f}°C")
        else:
            print("Invalid temperature unit. Use 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

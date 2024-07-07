FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
#convert_to_celsius(fahrenheit)

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
#convert_to_celsius(celsius)

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if unit == "C":
            #converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
        elif unit == "F":
            #converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
        else:
            print("Invalid input. Please enter C or F")
    except ValueError:
        print(f"Error: Invalid temperature. Please enter a numeric value.")
if __name__ == "__main__":
    main()

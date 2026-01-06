def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  try:
    celsius = float(celsius)
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
  except ValueError:
    return None

def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  try:
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * 5/9
    return celsius
  except ValueError:
    return None

if __name__ == "__main__":
  while True:
    temp_str = input("Enter the temperature: ")
    try:
      temp = float(temp_str)
      break
    except ValueError:
      print("Invalid input. Please enter a number.")

  while True:
    conversion_type = input("Convert to (C/F): ").upper()
    if conversion_type in ('C', 'F'):
      break
    else:
      print("Invalid input. Please enter 'C' or 'F'.")

  if conversion_type == 'F':
    fahrenheit = celsius_to_fahrenheit(temp)
    if fahrenheit is not None:
      print(f"{temp} Celsius is {fahrenheit} Fahrenheit")
    else:
      print("Invalid temperature input.")
  elif conversion_type == 'C':
    celsius = fahrenheit_to_celsius(temp)
    if celsius is not None:
      print(f"{temp} Fahrenheit is {celsius} Celsius")
    else:
      print("Invalid temperature input.")

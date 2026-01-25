import random
import string

def generate_password(length):
  """Generates a random password of the specified length."""
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password

def is_valid_length(length):
  """Checks if the given length is a valid integer."""
  try:
    length = int(length)
    if length > 0:
      return True
    else:
      return False
  except ValueError:
    return False


if __name__ == "__main__":
  while True:
    length = input("Enter the desired password length: ")
    if is_valid_length(length):
      length = int(length)
      break
    else:
      print("Invalid input. Please enter a positive integer.")

  password = generate_password(length)
  print("Generated password:", password)

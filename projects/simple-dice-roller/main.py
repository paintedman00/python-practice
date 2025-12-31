import random

def roll_dice(num_dice, num_sides):
  """Rolls a specified number of dice with a specified number of sides.

  Args:
    num_dice: The number of dice to roll.
    num_sides: The number of sides on each die.

  Returns:
    A list of integers representing the results of each die roll.
  """
  rolls = []
  for _ in range(num_dice):
    rolls.append(random.randint(1, num_sides))
  return rolls


def get_valid_integer_input(prompt):
  """Prompts the user for integer input and validates it.

  Args:
    prompt: The prompt to display to the user.

  Returns:
    An integer representing the user's input.
  """
  while True:
    try:
      user_input = int(input(prompt))
      if user_input > 0:
        return user_input
      else:
        print("Please enter a positive integer.")
    except ValueError:
      print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
  num_dice = get_valid_integer_input("How many dice do you want to roll? ")
  num_sides = get_valid_integer_input("How many sides per die? ")

  rolls = roll_dice(num_dice, num_sides)
  print("Rolls:", rolls)
  print("Sum:", sum(rolls))

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_recipe_cost(ingredients):
    total_cost = 0
    for ingredient, details in ingredients.items():
        total_cost += details['quantity'] * details['cost']
    return total_cost


def main():
    recipe_name = input("Enter the recipe name: ")
    ingredients = {}

    while True:
        ingredient_name = input("Enter ingredient name (or type 'done'): ")
        if ingredient_name.lower() == 'done':
            break

        quantity = get_float_input(f"Enter quantity of {ingredient_name}: ")
        cost = get_float_input(f"Enter cost per unit of {ingredient_name}: ")

        ingredients[ingredient_name] = {
            'quantity': quantity,
            'cost': cost
        }

    if not ingredients:
        print("No ingredients entered. Exiting.")
        return

    total_cost = calculate_recipe_cost(ingredients)
    print(f"\nRecipe: {recipe_name}")
    print(f"Total cost: ${total_cost:.2f}")

    while True:
      try:
          servings = int(input("Enter the number of servings: "))
          if servings <= 0:
              print("Please enter a positive number of servings.")
          else:
              break
      except ValueError:
          print("Invalid input. Please enter an integer.")

    cost_per_serving = total_cost / servings
    print(f"Cost per serving: ${cost_per_serving:.2f}")

if __name__ == "__main__":
    main()

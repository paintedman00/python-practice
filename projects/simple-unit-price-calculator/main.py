def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def calculate_unit_price(price, quantity):
    """Calculates the unit price of a product.

    Args:
        price: The total price of the product.
        quantity: The quantity of the product.

    Returns:
        The unit price, or None if the input is invalid.
    """
    if not is_valid_number(price) or not is_valid_number(quantity):
        print("Error: Price and quantity must be numbers.")
        return None

    price = float(price)
    quantity = float(quantity)

    if price <= 0 or quantity <= 0:
        print("Error: Price and quantity must be greater than zero.")
        return None

    return price / quantity


if __name__ == "__main__":
    product_name = input("Product Name: ")
    price = input("Price: ")
    quantity = input("Quantity: ")

    unit_price = calculate_unit_price(price, quantity)

    if unit_price is not None:
        print(f"\nThe unit price for {product_name} is: ${unit_price:.2f} per unit")

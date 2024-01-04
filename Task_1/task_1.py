# Configurations
PIZZA_COST = 12
DELIVERY_COST = 2.5
TUESDAY_DISCOUNT = 0.5
APP_DISCOUNT = 0.25
DISPLAY_TEXT_PIZZA = "How many pizzas ordered? "

def get_pizza_count(display_text):
    """ 
    Prompts the user to enter the number of pizzas ordered.
    
    Args:
        display_text (str): The message to display as the prompt.
        
    Returns:
        int: The validated and non-negative integer representing the count of pizzas.
    
    Raises:
        ValueError: If the user enters a non-integer value.

    This function continuously questions the user until a valid non-negative integer is provided.
    It handles input errors, such as non-integer input, and instructs the user to correct the input.
    """
    while True:
        try:
            value = int(input(display_text))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_yes_no_input(display_text):
    """
    Prompts the user for a Yes or No input (Y/N).

    Args:
        display_text (str): The prompt to display to the user.

    Returns:
        str: The validated user input, either 'Y' for Yes or 'N' for No.

    This function continuously questions the user until a valid input of 'Y' or 'N' is provided.
    The input is case-insensitive, and any leading or trailing whitespace is removed. 
    """
    while True:
        answer = input(display_text).strip().upper()
        if answer in {'Y', 'N'}:
            return answer
        else:
            print("Please input 'Y' or 'N'.")

def calculate_total_price(pizza_count, is_delivery, is_tuesday, used_app ):
    """
    Calculate the total cost of a pizza order.

    Args:
        pizza_count (int): The number of pizzas in the order.
        delivery_required (str): 'Y' if delivery is required, 'N' otherwise.
        is_tuesday (str): 'Y' if it is Tuesday, 'N' otherwise.
        used_app (str): 'Y' if the customer used the app, 'N' otherwise.

    Returns:
        float: The total cost of the pizza order.

    Notes:
        - Every pizza costs £12.
        - A 50% discount applies on Tuesdays.
        - Delivery costs £2.50 unless there are five or more pizzas in the order (free delivery).
        - A 25% discount applies if the order is placed via the BPP App.


    """
    # Base cost of Pizzas ordered
    total_cost = pizza_count * PIZZA_COST

    # Apply 50% Tuesday discount
    if is_tuesday.upper() == "Y":
        total_cost *= TUESDAY_DISCOUNT

    # Add delivery cost if required
    if is_delivery.upper() == "Y" and pizza_count < 5:
        total_cost *= DELIVERY_COST

    # Apply 25% BPP app discount
    if used_app.upper() == "Y":
        total_cost -= (total_cost * APP_DISCOUNT)

    return total_cost



def main():
    print("\nBPP Pizza Price Calculator")
    print("="*40)

    pizza_count = get_pizza_count("How many pizzas ordered? ")

    is_delivery = get_yes_no_input("Is delivery required? (Y/N) ")

    is_tuesday = get_yes_no_input("Is it Tuesday? (Y/N) ")

    used_app = get_yes_no_input ("Did the Customer use the app? (Y/N) ")

    total_price = calculate_total_price(pizza_count, is_delivery, is_tuesday, used_app)
    print("="*40)
    print(f"Total Price: £{total_price:.2f}")
    print("="*40)

if __name__ == "__main__":
    main()
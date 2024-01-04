def get_pizza_count(display_text):
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
    pass
def calculate_total_price(pizza_count, is_delivery, is_tuesday, used_app ):
    pass



def main():

    print("\nBPP Pizza Price Calculator")
    print("====================================")

    pizza_count = get_pizza_count("How many pizzas ordered? ")
    print(pizza_count)

    # is_delivery = get_yes_no_input("Is delivery required? (Y/N) ")

    # is_tuesday = get_yes_no_input("Is it Tuesday? (Y/N) ")

    # used_app = get_yes_no_input("Did the Customer use the app? (Y/N) ")

    # total_price = calculate_total_price(pizza_count, is_delivery, is_tuesday, used_app)
    # print("=====================================")
    # print(f"Total Price: £{total_price:.2f}")
    # print("=====================================")

if __name__ == "__main__":
    main()
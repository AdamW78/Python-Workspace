from random import uniform

# Set maximum item price, minimum item price, starting amount of money
min_price = 1
max_price = 10
starting_money = 25
# Initialize current money to the starting money value provided
current_money = starting_money
# Initialize counter variable for number of items purchased
num_items_purchased = 0
# While the user's current amount of money is greater than zero
while current_money > 0:
    # Generate random item price in X.XX format
    current_item_price = round(uniform(min_price, max_price), 2)
    # Check if the user purchase the current item
    if current_money > current_item_price:
        # If current money is greater than random item price
        # Subtract item price from current money, format to X.XX
        current_money -= current_item_price
        current_money = round(current_money, 2)
        num_items_purchased += 1
        # Print money remaining and last purchased item cost
        print(f"Purchased an item for ${current_item_price:.2f}! "
              f"Your money remaining is ${current_money:.2f}.")
    else:
        # If current money is insufficient to purchase current item
        # Ask if they want to try to scan more items
        # Print current money remaining and wait for input
        # Valid input: "y" or "n"
        print(f"Your current item (price (${current_item_price:.2f}) is too expensive to buy! Continue scanning items?")
        print(f"Your money remaining is ${current_money:.2f}")
        y_n = input("Enter \"y\" or \"n\": ").casefold()
        if y_n == "n":
            # If user does not want to continue, exit while loop
            break
        elif not y_n == "y":
            # Invalid input case
            print("Error: Invalid input, exiting loop!")
            break
# Print final money value and number of items purchased
print(f"You finished scanning items with ${current_money:.2f}!")
print(f"You bought {num_items_purchased} items!")
# creat a function called calculate_chocolate_bars
def calculate_chocolate_bars(total_money, price_per_bar):

    # Calculate the number of bars by dividing the total money by the price per bar
    num_bars = total_money // price_per_bar

    # Calculate the remaining change
    remaining_change = total_money % price_per_bar

    return (num_bars, remaining_change)

# Example usage:
total_money = 100
price_per_bar = 16
bars_bought, change_left = calculate_chocolate_bars(total_money, price_per_bar)
print(f"With total money ${total_money}, you can afford {bars_bought} chocolate bars and have ${change_left} change left over.")

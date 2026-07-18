stock_prices = {
    "TCS": 3500,
    "INFY": 1600,
    "RELIANCE": 2900,
    "HDFC": 1800
}

total_value = 0

# File open
file = open("portfolio.txt", "w")

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        value = stock_prices[stock] * quantity
        total_value += value

        print("Value of", stock, "=", value)

        # Save data to file
        file.write("Stock: " + stock +
                   ", Quantity: " + str(quantity) +
                   ", Value: " + str(value) + "\n")

    else:
        print("Stock not found!")

print("\n===== Portfolio Summary =====")
print("Total Investment Value =", total_value)

# Save total value
file.write("\nTotal Investment Value = " + str(total_value))

# Close file
file.close()

print("Portfolio saved successfully in portfolio.txt")
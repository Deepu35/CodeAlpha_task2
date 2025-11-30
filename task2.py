# Simple Stock Portfolio Tracker

# Hardcoded stock prices
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 310,
    "AMZN": 130
}

total_value = 0

print("Available stocks and prices:")
for stock, price in prices.items():
    print(stock, ":", price)

print("\nEnter 'done' to stop.\n")

while True:
    stock = input("Enter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in prices:
        print("Stock not found!\n")
        continue

    qty = int(input("Enter quantity: "))
    total_value += prices[stock] * qty
    print("Added:", stock, "x", qty, "\n")

print("Total Investment Value:", total_value)

# Optional: Save to file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: {total_value}")

print("\nSaved to portfolio.txt")

class Stock:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def value(self):
        return self.quantity * self.price

def display_portfolio(stocks):
    print("\n--- Stock Portfolio ---")
    total_value = 0
    for stock in stocks:
        stock_value = stock.value()
        total_value += stock_value
        print(f"{stock.name} - Quantity: {stock.quantity}, Price: ${stock.price:.2f}, Value: ${stock_value:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    portfolio = []
    print("Welcome to the Stock Portfolio Tracker")
    while True:
        print("\nMenu:")
        print("1. Add stock")
        print("2. View portfolio")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            name = input("Enter stock name: ")
            quantity = int(input("Enter stock quantity: "))
            price = float(input("Enter stock price: "))
            portfolio.append(Stock(name, quantity, price))
            print(f"{name} added to your portfolio.")
        elif choice == "2":
            display_portfolio(portfolio)
        elif choice == "3":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

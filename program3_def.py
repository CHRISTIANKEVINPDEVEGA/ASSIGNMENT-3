import math

def ask_budget(): 
    amount_money = float(input("Enter the amount of money you have: ₱"))
    return amount_money


def ask_desired_price():
    apple_price = float(input("How much will you pay for an apple? ₱"))
    return apple_price

def display(budgetF, priceF):
    apple_stock= 10
    price_X_stock = priceF * apple_stock
    user_change = budgetF - price_X_stock
    print(f"You can buy {apple_stock} apples and your change is ₱{user_change:.2f}.")

budget = ask_budget()
price = ask_desired_price()

display(budget, price)



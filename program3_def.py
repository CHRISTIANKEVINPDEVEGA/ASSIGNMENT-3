import math

def Apple_machine(): 
    amount_money = float(input("Enter the amount of money you have: ₱"))
    apple_price = float(input("How much will you pay for an apple? ₱"))
    apple_stock = 10
    Calculation= amount_money - (apple_stock * apple_price)
    print(f"You can buy {apple_stock} apples and your change is ₱{Calculation:.2f}.")


Apple_machine()    
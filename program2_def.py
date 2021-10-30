import math

def fruits_total_price():
    apple = int(input("How many apples do you want to buy? "))
    NumberOfApple_X_ApplePrice= apple*20
    print(f"₱20 X {apple} = ₱{NumberOfApple_X_ApplePrice}")

    orange = int(input("How many oranges do you want to buy? "))
    NumberOfOrange_X_OrangePrice= orange*25
    print(f"₱25 X {orange} = ₱{NumberOfOrange_X_OrangePrice}")

    total_amount = NumberOfApple_X_ApplePrice + NumberOfOrange_X_OrangePrice
    print(f"The total amount is ₱{total_amount}.")
    

fruits_total_price()
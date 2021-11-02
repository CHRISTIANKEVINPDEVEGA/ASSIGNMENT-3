import math

def apple_price():
    ask4_apple = int(input("How many apples do you want to buy? "))
    return ask4_apple 

def orange_price():
    ask4_orange = int(input("How many oranges do you want to buy? "))
    return ask4_orange

def Display(_Ask_apple , _Ask_orange):
    Total_calculation = (_Ask_apple * 20) + (_Ask_orange * 25)
    print(f"The total amount is ₱{Total_calculation}.")
    

Ask_apple = apple_price()
Ask_orange = orange_price()

Display(Ask_apple, Ask_orange )


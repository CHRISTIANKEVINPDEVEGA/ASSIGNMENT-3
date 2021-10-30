def ask_name():
    Name = input("what is your name? ")
    return Name

def ask_age():
    Age = input("what is your age? ") 
    return Age

def ask_address():
    Address = input("what is your address? ") 
    return Address

def display(NAME, AGE, ADDRESS):
   print(f"Hi, my name is {NAME}. I am {AGE} years old and I live in {ADDRESS}.")


Name = ask_name()

Age = ask_age()

Address = ask_address()

display(Name, Age, Address)
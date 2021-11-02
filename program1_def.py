def ask_name():
    _Name = input("what is your name? ")
    return _Name

def ask_age():
    _Age = input("what is your age? ") 
    return _Age

def ask_address():
    _Address = input("what is your address? ") 
    return _Address

def display(NAMEf, AGEf, ADDRESSf):
   print(f"Hi, my name is {NAMEf}. I am {AGEf} years old and I live in {ADDRESSf}.")


name = ask_name()

age = ask_age()

address = ask_address()

display(name, age, address)
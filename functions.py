"""
Syntax:

def function_name(arguments):
    # function body
    return

"""

def greet():
    print("Hello, how are you!")

# print("Program starts")
# greet()
# print("Program finished")
# greet()

def greet_by_name(name):
    print("Hello", name, "how are you!")

# greet_by_name("Sandipan")

def get_discounted_price(price, discount = 5):
    discounted_price = price - (price * discount / 100)
    return discounted_price

# calculated_amount = get_discounted_price(1000)
# print("The discounted price is:", calculated_amount)

def get_price_after_tax(price, tax = 2): # 1000, 2
    price_after_tax = price + (price * tax / 100) # 1020
    return price_after_tax

def display_price_after_tax():
    price = int(input("Enter the price:"))
    final_price_after_tax = get_price_after_tax(price) # 1020
    print("The price after tax is:", final_price_after_tax, "$")

display_price_after_tax()

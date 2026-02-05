"""
Cart mini project -2

Create a ecommerce cart that takes which items they wanna buy  
Ask for their name  
How many qty they wanna buy  
At what price they are buying  
Show the total cart including $ sign
"""
# Asking for user name
user_name = input("Hello, what is your name: ")

# Products they want to buy
products = input("What are the products you want to purchase: ")

# Quantity they want to purchase
quantity = int(input("Enter the quantity you want to purchase: "))

# Price they are buying
price = float(input("What price do you purchase at: "))

# Results of the price by quantity
result = price * quantity

print(f"Hello {user_name}, your total amount ${result}. Thank you for shopping with us.")


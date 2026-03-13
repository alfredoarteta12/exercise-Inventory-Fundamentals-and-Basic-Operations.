print("Welcome to the sales program")

# First, the user will enter the product name, price, and quantity.
product_name = input("Enter the product name: ")
product_price = float(input("Enter the product price: "))

# Here we check that the price is not negative.
# If it is negative, the user will be asked to enter a valid value.
while product_price < 0:
    print("The price can't be negative. Please enter a valid price.")
    product_price = float(input("Enter the product price: "))

product_quantity = int(input("Enter the product quantity: "))

# We also check that the quantity is not negative.
# If it is, the user will be asked to enter a valid quantity.
while product_quantity < 0:
    print("The quantity can't be negative. Please enter a valid amount.")
    product_quantity = int(input("Enter the product quantity: "))

# Once we have valid data, we calculate the total sale
# by multiplying the price by the quantity.
total_sale = product_price * product_quantity

print(f"You bought: product: {product_name}, price: {product_price}, quantity: {product_quantity}")

# Finally, we show the total cost of the sale.
print(f"The total sale is: {total_sale}")


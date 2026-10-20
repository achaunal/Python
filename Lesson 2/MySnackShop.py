snack_name="Chips"
price=1.50
quantity=10
is_available = True
print("Snack: ", snack_name)
print("Price: $", price)
print("In Stock: ", quantity)
print("Available?", is_available)
print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))
total=price * quantity
print("Total Value: $", total)
print("Sale Price: $", price - 0.25)
print("Double Stock:", quantity * 2)
print("Is The Price Under $2?", price < 2)
print("More Than 5 In Stock?", quantity > 5)
print("Is The Price Exactly $1.50?", price == 1.50)
shop_name = "quick" + " " + "Bites"
print("Shop Name: ", shop_name)
print("Letters In Snack Name:", len(snack_name))
print("First Letter: ", snack_name[0])
price_a=1.50
price_b=3.00
print("Before: ", price_a, "and ", price_b)
temp=price_a
price_a=price_b
price_b=temp
print("After: ", price_a, "and ", price_b)

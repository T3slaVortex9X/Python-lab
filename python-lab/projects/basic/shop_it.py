print("=========================================")
print("        Wellcome to shopping list          ")
print("==========================================")

item = input("What item you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"you have bought {quantity} * {item}/s")
print(f"your total is: ${round(total, 2)}")
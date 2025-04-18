menu = {"Tea":120, "Coffee":150, "Snacks":200}
Total_bill=0
order = str(input("Do you want to order something: "))
if order=="yes":
    print("Here's the menu",menu)
    your_order = str(input("What would you like to order: "))
    if your_order == "Tea" or your_order == "tea":
        Total_bill+=120
    elif your_order == "Coffee" or your_order == "coffee":
        Total_bill+=150
    elif your_order == "Snacks" or your_order == "snacks":
        Total_bill+=200
    else:
        print("Dish not available")
your_order_1 = str(input("Would you like to order something else: "))
while your_order_1=="yes":
    print("Here's the menu again", menu)
    your_order_2 = str(input("What would you like to order: "))
    if your_order_2 == "Tea" or your_order_2 == "tea":
        Total_bill+=120
    elif your_order_2 == "Coffee" or your_order_2== "coffee":
        Total_bill+=150
    elif your_order_2 == "Snacks" or your_order_2 == "snacks":
        Total_bill+=200
    else:
        print("Dish not available")
    your_order_1 = str(input("Would you like to order something else: "))
else:
    print("Thank you for ordering")
print("Here's your Total bill:",Total_bill)

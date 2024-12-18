name = input("Enter your name :   ")
age = eval(input("Enter your age :   "))
nameitem = input("Enter the name of the item :   ")
priceitem = eval(input("Enter the price of the item :   "))
amountgiven = eval(input("Enter the amount you gave :     "))
buyGrocery = str(input("Did you buy a grocery (yes/no) :     "))

tax = priceitem * 0.123
total = tax + priceitem
discount = total * 0.052
change = amountgiven - total

if buyGrocery.lower() == "yes":
	print("Hi" , name , "you purchased a" , nameitem ,  "with a price of" , priceitem ,  "plus the" , tax ,  "tax")
	
	if age >= 60:
		total = total - discount
		changewithdiscount = change + discount
		print("\nYou have a discount of", round(discount, 2))
		print("Your total item price: ", round(total, 2))
		print("Your change: ", round(changewithdiscount, 2))

	else:
		print("\nMust be a senior citizen to have a discount")
		print("Your total item price: ", round(total, 2))
		print("Your change: ", round(change, 2))

elif buyGrocery.lower() == "no":
	print("Thank you for visiting Kitsune Store!")
else:
	print("\nPlease answer correctly and try again!")


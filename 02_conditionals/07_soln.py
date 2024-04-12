order = input("Enter your coffee size: Small, Medium, Large")
option = input("Enter y for Extra shot of Espresso else enter n")
coffeeSize = ""
extraShotCount = 0

if order == "Small":
    coffeeSize = "Small"
elif order == "Medium":
    coffeeSize = "Medium"
elif order == "Large":
    coffeeSize = "Large"
else:
    coffeeSize = "Invalid"
    exit()

extraShotCount = 1 if option == "y" else 0


print("Your order is a", coffeeSize, "cofee with", extraShotCount, "extraShout")
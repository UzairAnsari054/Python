fruitColor = "Brown"
fruitStatus = ""

if fruitColor == "Green":
    fruitStatus = "Unripe"
elif fruitColor == "Yellow":
    fruitStatus = "Ripe"
elif fruitColor == "Brown":
    fruitStatus = "Overripe"
else:
    fruitStatus = "Invalid"

print(fruitStatus)
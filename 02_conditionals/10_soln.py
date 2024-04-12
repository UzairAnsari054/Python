petSpecie = "Dog"
petAge = 12

if petSpecie == "Dog":
    if petAge < 2:
        print("Puppy food")
    else:
        print("Senior Dog Food")    
elif petSpecie == "Cat":
    if petAge < 2:
        print("Kitnen food")
    else:
        print("Senior Cat Food")    
else:
    print("Specie not in database")

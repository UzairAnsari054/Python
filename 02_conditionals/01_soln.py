age = 10
ageGroup = ""
if age < 13:
    ageGroup = "Child"
elif age < 20:
    ageGroup = "Teenager"
elif age < 60:
    ageGroup = "Adult"
else:
    ageGroup = "Senior"

print(ageGroup)
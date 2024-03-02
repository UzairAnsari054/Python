def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Uzair", age = 25)
print_kwargs(name="Uzair")
print_kwargs(name="Sonu", age = 30)
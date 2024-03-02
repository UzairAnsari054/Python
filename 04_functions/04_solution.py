import math

def circle_stats(radius):
    area = math.floor(math.pi * radius ** 2)
    circumference = math.floor(2 * math.pi * radius)
    return area, circumference

area, circumference = circle_stats(3)
print("Area: ", area, "Circumference: ", circumference )
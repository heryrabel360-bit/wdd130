import math
from datetime import datetime

current_date_and_time = datetime.now()
print(f"{current_date_and_time:%Y-%m-%d}")

width = float(input("Enter the width of the tire in mm (ex 205): "))
print(f"Width {width}")

ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
print(f"Ratio {ratio}")

diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
print(f"Diameter {diameter}")

volume = (math.pi * width**2 * ratio *
          (width * ratio + 2540 * diameter)) / 10000000000

print(f"The approximate volume is {volume:.2f} liters.")

with open("volumes.txt", "a") as file:
    file.write("Hello Python!\n")

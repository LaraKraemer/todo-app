colors = [11, 34, 98, 43, 45, 54, 54]

for item in colors:
    if item > 50:
        print(item)

try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That looks like a square")

    rectangle = width * length
    print(rectangle)
except ValueError:
    print("Please enter a number")


list  = ["sean", "ben", "john"]
list.sort()

for index, item in enumerate(list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)
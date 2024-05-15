def get_max():
    grades = [9.6, 9.2, 9.7]
    max_local = max(grades)
    min_local = min(grades)
    comparison = f"Max:{max_local}, Min:{min_local}"
    return comparison


print(get_max())



def get_average():
    with open("files/data.txt", "r") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / 4
    return average_local

average = get_average()
print(average)
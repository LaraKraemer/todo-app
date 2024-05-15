def get_temp(temperature):
    if temperature > 25:
        return "Hot"
    if 15 <= temperature <=25:
        return "Warm"
    if temperature < 15:
        return "Cold"

print(get_temp(5))
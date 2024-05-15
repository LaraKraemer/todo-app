from experiements.Decoupling_convert_function138 import convert
from experiements.Decoupling_parse_function138 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed["feet"], parsed["inches"])


print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")
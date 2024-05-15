password = input("Enter your password: ")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False
    

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = True

upper = False
for i in password:
    if i.isupper():
        upper = True

result["uppers"] = True

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")
print(result)
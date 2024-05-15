date = input("Please enter today's date: ")
mood = input("How do you rate your mood from 1 to 10: ")
text = input("Let your thoughts flow:\n")

with open(f"../files/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(text)


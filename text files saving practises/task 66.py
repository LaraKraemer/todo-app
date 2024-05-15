new_member = input("Please add the name of a new member: ")

with open("../files/members.txt", "a") as file:
    file.write(new_member + "\n")





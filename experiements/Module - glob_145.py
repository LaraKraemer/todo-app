import glob

my_files = glob.glob('/Users/lara/Desktop/Python Bootcamp/todolist/files/*.txt')

for filepath in my_files:
    with open(filepath, "r") as file:
        print(file.readlines())
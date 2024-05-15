filenames = ["1.report", "1.doc", "1.presentation"]

# syntax of list comprehansion
filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]

print(filenames)

names = ["john smith", "jay santi", "eva kuki"]

names = [new_names.title() for new_names in names]
print(names)


user_entries = ['10', '19.1', '20']

print(sum(user_entries))
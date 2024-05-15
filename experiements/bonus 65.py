#creating new files with content

contents = ["Hello", "Bye", "Good Morning"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../test_file/{filename}", "w")
    file.write(content)


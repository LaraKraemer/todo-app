filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# Iterate over the list and create a new file for each filename
for filename in filenames:
    with open(filename, 'w') as file:
        # Write some content to the file (optional)
        file.write("Hello ")
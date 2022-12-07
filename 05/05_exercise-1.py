filenames = ['document', 'report.txt', 'presentation.txt']

for index, files in enumerate(filenames):
    row = f"{index}-{files.capitalize()}.txt"
    print(row)

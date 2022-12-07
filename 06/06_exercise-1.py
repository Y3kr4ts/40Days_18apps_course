file = open("files/essay.txt", 'r')
content = file.readline()
file.close()
print(content.title())

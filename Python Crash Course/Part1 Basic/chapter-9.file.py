with open("pi.txt", "r") as file_object:
    contents = file_object.read()
    print(contents.replace(' ', ''))
    file_object.close()
    contents = file_object.read()
    print(contents)
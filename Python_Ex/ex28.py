def write_file():
    file = open("message.txt", "w")
    file.write("Hello World")
    file.close()
    print("File written successfully")

write_file()
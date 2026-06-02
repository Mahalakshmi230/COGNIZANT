def read_file():
    try:
        file = open("message.txt", "r")
        content = file.read()
        file.close()
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print("File not found")

read_file()
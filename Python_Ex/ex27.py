def string_length(text):
    if isinstance(text, str) and text.strip() != "":
        length = len(text)
        print(f"Length of string: {length}")
    else:
        print("Invalid input")

text = "Hello World"
string_length(text)
file = input("Enter your file name: ")
file = file.split(".")[-1].strip().lower()

match file:
    case "py" | "ipynb":
        print("Python File")
    case "png" | "jpg":
        print("Image File")
    case "txt" | "md":
        print("Text File")
    case _:
        print("Unknown File Format")
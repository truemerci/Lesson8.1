try:
    file = open("example.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("No such file exists")

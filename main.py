try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("No such file exists")
finally:
    file.close()

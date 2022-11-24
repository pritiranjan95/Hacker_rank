def readfile(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"The given file {filename} is not found")



readfile("1.txt")
readfile("3.txt")
readfile("2.txt")

#Another way::::::

try:
    a = open("1.txt")
    print(a.read())
except FileNotFoundError:
    print(f"given file not found")

try:
    a = open("3.txt")
    print(a.read())
except FileNotFoundError:
    print(f"given file not found")

try:
    a = open("2.txt")
    print(a.read())
except FileNotFoundError:
    print(f"given file not found")




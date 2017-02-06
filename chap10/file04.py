# 10-6

num_1 = input ("Please enter the first number (int): ")
num_2 = input ("Please enter the second number (int): ")

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
except ValueError:
    print ("At least one of your input is invalid number.")
else:
    print(str(num_1) + " + " + str(num_2) + " = " + str(num_1 + num_1))


# 10-10
filename = "alice.txt"

try:
    with open(filename) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    print ("File <" + filename + "> not found!")
else:
    print(str(contents.lower().count("alice")))



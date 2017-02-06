with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# On Linux / OS X
# with open('text_files/filename.txt') as file_object:

# On Windows
# with open('text_files\filename.txt') as file_object:

# Windows systems will sometimes interpret forward slashes in file paths correctly. If
# you’re using Windows and you’re not getting the results you expect, make sure you try
# using backslashes.

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# When Python reads from a text file, it interprets all text in the file as a string. If you
# read in a number and want to work with that value in a numerical context, you’ll
# have to convert it to an integer using the int() function or convert it to a float using
# the float() function.

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
# This flexibility allows you to use quotes and apostrophes within your strings:

# 'I told my friend, "Python is my favorite language!"'
# "The language 'Python' is named after Monty Python, not the snake."
# "One of Python's strengths is its diverse and supportive community."

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print (full_name)

print("Hello, " + full_name.title() + "!")

print("\t<-this is a tab. \n This is a new line.")

age = ' 30 '
print(age.rstrip()) # rstrip = right stripping | lstrip = left strpping | strip = both sides

# fill in a dictionary using while + input

responses = {}

polling_active = True

while polling_active:
    name = input("Please enter your name: ")
    response = input("Which mountain would you like to climb today? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
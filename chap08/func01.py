# parameter username of this function
def greet_user(username):
"""Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse') # argument = 'jesse'


# positional arguments
def describe_pet(animal_type, pet_name):
"""Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# default values
# def describe_pet(pet_name, animal_type='dog'):
# those parameters which has a default value should be listed after other parameters
# so that when you are using positional arguments, it will work out prefectly


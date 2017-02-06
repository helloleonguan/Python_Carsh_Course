# if in Python 2.7 class ClassName(object): is the right way

# this is Python 3.x

class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

# 9-3
class User():
    """ A user model """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title())

    def describe_user(self):
        print("The name of this user is " + self.first_name.title() + " " + self.last_name.title())

user_1 = User('Leon', 'Guan')
user_1.greet_user()
user_1.describe_user()


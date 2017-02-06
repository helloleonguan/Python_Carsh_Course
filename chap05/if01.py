cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Testing for equality is case sensitive in Python

# Conditional Operator: == != < > <= >= and or

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users: # in / not in
    print(user.title() + ", you can post a response if you wish.")

# Boolean variables
game_active = True
can_edit = False

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# 5-3 -> 5-7
alien_color = 'red'

if alien_color == 'green':
    print("You have just earned 5 points.")

if alien_color == 'red':
    print("You have just earned 5 points.")

if alien_color == 'green':
    print("You have just earned 5 points.")
elif alien_color == 'yellow':
    print("You have just earned 10 points.")
elif alien_color == 'red':
    print("You have just earned 15 points.")

age = 21

if age < 2:
    print("you are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

favorite_fruits = ["apple", "banana", "grape"]

if "lemon" not in favorite_fruits:
    print("lemon is not my favorite.")

if "apple" in favorite_fruits:
    print("apple is my favorite.")



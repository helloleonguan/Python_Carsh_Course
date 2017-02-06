# aribtrary parameter should be placed last.
# * = a tuple
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# ** = a dictionary
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# key-value pairs can be passed to this function
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# 8-14
def make_car(manufacturer, model_name, **details):
    """Build a car contianing everything we know."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name
    for k, v in details.items():
        car[k] = v
    return car

my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)


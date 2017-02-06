# A simple dictionary

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# add more key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# modify a value
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# remove key-value pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# 6-1 -> 6-3
person = {
    'first_name' : 'Leon',
    'last_name'  : 'Guan',
    'city'       : 'HZ',
    'age'        : 21,
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


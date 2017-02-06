# Slicing

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

# Copying List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # not a reference
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Sometimes you’ll want to create a list of items that cannot
# change. Tuples allow you to do just that. Python refers to values that cannot
# change as immutable, and an immutable list is called a tuple.
# Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
	print(dimension)

# redefining the entire tuple is allowed
dimensions = (400, 100)

# 4-13
food_list = ('chips', 'coke', 'burger', 'wrap', 'steak')

for food in food_list:
	print (food)

food_list = ('chips', 'soup', 'burger', 'wrap', 'salad')

for food in food_list:
    print (food)


# Style Guide
# 1. Indentation : use 4 spaces
# 2. Line Length: limit all of your comments to 72 characters per line
# 3. look PEP 8 guidelines. at https://python.org/dev/peps/pep-0008/

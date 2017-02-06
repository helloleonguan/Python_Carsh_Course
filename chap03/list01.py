# List Part I

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())

print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 3-1
names = ['Alice', 'Bob', 'Cindy', 'Desemond']
print (names[0])
print (names[1])
print (names[2])
print (names[3])

# 3-2
print ("Hi, " + names[0] + " how is your day?")
print ("Hi, " + names[1] + " how is your day?")
print ("Hi, " + names[2] + " how is your day?")
print ("Hi, " + names[3] + " how is your day?")

# 3-3
trans = ['bike', 'plane', 'motorcycle']
print ("I would like to have a " + trans[0] + ".")
print ("I would like to have a " + trans[1] + ".")
print ("I would like to have a " + trans[2] + ".")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('Luci')
print (motorcycles)

motorcycles.insert(0, 'Howi')
print (motorcycles)

# remove an item that you do not want to use
del motorcycles[0]
print(motorcycles)

# remove an item but you want to use
popped_motorcycle = motorcycles.pop() # .pop(1)
print(motorcycles)
print(popped_motorcycle)

# remove an item by its value
motorcycles.remove('yamaha')
print (motorcycles)

# The remove() method deletes only the first occurrence of the value you specify. If there’s
# a possibility the value appears more than once in the list, you’ll need to use a loop to
# determine if all occurrences of the value have been removed.


# 3-4
# 3-5
# 3-6
# 3-7

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# permanent
cars.sort(reverse=True)
print(cars)

# temporary
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Sorting a list alphabetically is a bit more complicated when all the values are not in
# lowercase. There are several ways to interpret capital letters when you’re deciding on
# a sort order, and specifying the exact order can be more complex than we want to deal
# with at this time. However, most approaches to sorting will build directly on what you
# learned in this section.

cars.reverse()
print(cars)
print(len(cars))

# 3-8
# 3-9
# 3-10

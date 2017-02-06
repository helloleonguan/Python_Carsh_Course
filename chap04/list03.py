# loop through the list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

print("Thank you, everyone. That was a great magic show!")

# range(initValue, stopValue)
# 1
# 2
# 3
# 4
for value in range(1,5):
	print(value)

numbers = list(range(1,6))
print(numbers)

# range(initValue, stopValue, incrementValue)
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

# stats functions
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# min(digits) = 0
# max(digits) = 9
# sum(digits) = 45

squares_1 = [value**2 for value in range(1,11)]
print(squares_1)

# 4-3
print ("\n4-3\n")
for num in range (1,21):
	print (num)

# 4-5
print ("\n4-5\n")
nums = list(range(1,1000001))
print (min(nums))
print (max(nums))
print (sum(nums))

# 4-6
print ("\n4-6\n")
for num in range (1,20,2):
	print(num)

# 4-7
print ("\n4-7\n")
nums = list(range(3,31,3))
for num in nums:
	print (num)

# 4-9
print ("\n4-9\n")

cubes = [cube**3 for cube in range(1,11)]
print(cubes)

# if <list> will check whether the list is empty.
# if list is empty = FALSE
# if list is not empty = TRUE

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

# 5-8 -> 5-11

users = ["alice", "bob", "cindy", "david", "admin"]

if users:
    for user in users:
        if user == 'admin':
            print ("hello admin, would you like to see a status report?")
        else:
            print ("hello " + user + " , thanks for logging in.")
else:
    print("We need more users.")

current_users = ["John", "BEth", "Kelly", "Olive", "cathy"]
new_users = ["joHn", "cathy", "cindy", "Ben", "Jess"]

for new_user in new_users:
    if new_user.lower() in (current_user.lower() for current_user in current_users):
        print(new_user + " is already a user, enter a new username.")
    else:
        print ("welcome " + new_user)


# 1
names = ["john smith", "jay santi", "eva kuki"]
# make the names captial, first and last
names = [name.title() for name in names]
print(names)

# 2
usernames = ["john1990", "alberta1970", "magnola2000"]
# print out the length of each value in the list
print([len(name) for name in usernames])

# 3
user_entries = ["10", "19.1", "20"]
# print the list out but as floats
print([float(entry) for entry in user_entries])

# 4
# get the sume of the user_entries
user_numbers = [float(number) for number in user_entries]
print(sum(user_numbers))

# 1
temp = [10, 12, 13]
temp = [str(item) + "\n" for item in temp]
print(temp)

# 2
# convert all numbers to ints
numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)

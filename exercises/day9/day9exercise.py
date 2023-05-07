# bonus example
password = input("Enter new password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

char = False
for i in password:
    if i.isupper():
        char = True
result.append(digit)

if all(result):
    print("Strong password")
else:
    print("Weak password")



# dictionary lesson
my_dict = {"height":10, "width":20, "depth":30}
print(my_dict)
my_dict["area"] = 100
print(my_dict)
# use dictionaries when you need to label different items in a container
# use lists when all the items in the container are labeled the same

# bonus example with dictionary
password = input("Enter a new password:")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

char = False
for i in password:
    if i.isupper():
        char = True
result["char"] = char

print(result)
if all(result.values()): # check values of dictionary
    print("Strong password")
else:
    print("Weak password")

# exercise 1
# write a password checker that checks if the pwd is great than 7

password = input("Enter a password: ")
print(len(password))
if len(password) > 7:
    print("Great password")
elif len(password) == 7:
    print("Password is okay, but not strong enough")
else:
    print("Weak password")


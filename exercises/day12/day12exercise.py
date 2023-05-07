# bonus example
# extract values from string

feet_inches = input("Enter feet and inches: ")

def convert(feet_inches):
    values = feet_inches.split(" ")
    feet = float(values[0])
    inches = float(values[1])

    meters = feet * 0.3048 + inches * 0.0254
    return f"{feet} feet and {inches} inches is equal to {meters} meters"

print(convert(feet_inches))
    
# 1
# make program converts liter to cubic meter

def cubic_meter(liters):
    return liters * 1000
print(f"cubic meters =", cubic_meter(20))

# 2
# ask for pwd
# check pwd str
# strong pwd if it passes all checks
# >= 8 length
# 1 upper case
# 1 digit

user_password = input("please enter a password: ")
def password_checker(user_password_arg):
    check_list = []

    length = False
    if len(user_password_arg) >= 8:
        length = True
    check_list.append(length)

    has_upper = False
    for i in user_password_arg:
        if i.isupper():
            has_upper = True
    check_list.append(has_upper)

    has_digit = False
    for i in user_password_arg:
        if i.isdigit():
            has_digit = True
    check_list.append(has_digit)
    
    if all(check_list):
        print("Strong password")
    else:
        print("Weak Password")
    
    print(check_list)

password_checker(user_password)

# bugs
# 1
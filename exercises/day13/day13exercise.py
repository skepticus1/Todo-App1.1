# bonus example
# extract values from string

feet_inches = "6 6"


def parse(size):
    values = size.split(" ")
    feet = float(values[0])
    inches = float(values[1])
    return {"foot": feet, "inch": inches}


def convert(foot, inch):
    return foot * 0.3048 + inch * 0.0254
    
size = parse(feet_inches)
print(size)
print(size["foot"])

meters = convert(size["foot"], size["inch"])
print(meters)

# 1, 2, 3
def age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    if age > 120:
        return "You're very old"
    else:
        return age

yob = int(input("What is your year of birth? "))
print(age(yob))

# 4
# create a list from names a user enters
def name_list(names):
    return names.split(",")

people = input("enter names separated by commas (no spaces): ")
print(name_list(people))

# bugs
# 1
def calc_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t

time = calc_time(100)
print(time)
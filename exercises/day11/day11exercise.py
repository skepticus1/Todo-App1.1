def get_average():
    with open("app1/exercises/files/day11data.txt", "r") as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    total = 0
    for i in values:
        total = total + i

    average = sum(values) / len(values)

    return total / len(values)

print(get_average())


# 1
# print max value
grades = [9.6, 9.2, 9.7]
def get_max():
    return max(grades)
print(get_max())

# 2
# now return max and min from grades
def get_max_min():
    return print(f"Max: {max(grades)}, Min: {min(grades)}")
get_max_min()

# 1 bug fix
# get max value of cel
# convert cel to fah and print

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    print(maximum)
    return maximum

celsius = get_maximum()

fah = celsius * 1.8 + 32
print(fah)
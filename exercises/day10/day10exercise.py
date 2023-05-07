# percent calculator
# enter total value
# enter value
# that is 40.0 percent
# try except for type errors

try:
    total = float(input("Please enter a total value: "))
    value = float(input("Please enter a value:"))
    percent = value / total * 100
    print(f"That is {percent}%")
except TypeError:
    print("Numbers only.")
except ZeroDivisionError:
    print("You can't divide by zero.")

# bug fixing exercise 1
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} isn't on the list.")
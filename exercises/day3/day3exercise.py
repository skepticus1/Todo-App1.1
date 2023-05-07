# 1.
# create program that:
# prompts user to input country they are from
# if the user enters USA the prog prints out Hello
# if the user enters India, the prog prints out Namste
# if the user enters Cermany, the program prints out Hallo

user_input = input("Enter Country: ")

match user_input:
    case 'USA':
        print("Hello")
    case 'India':
        print("Namaste")
    case 'Germany':
        print("Hallo")


#    2.
#    create a program that prints out the following list
#    ingredients = ["john smith", "sen plakay", "dora ngacely"]

ingredients = ["john smith", "sen plakay", "dora ngacely"]

for i in ingredients:
    print(i.title())
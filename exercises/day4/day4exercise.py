"""
Coding Exercise 1
create a program
1. prompts user to input dollar amount
2. calcs the amount in euors, given exchange rate of .95
3. prints out the amount in euros
"""

dollars = float(input("Enter a dollar amount: "))
euros = dollars * 0.95
print("You have ", euros, " euros worth of dollars")

"""
Coding exercise 2
rankings = ['John', 'Sen', 'Lisa']
1. contains above list
2. prompts the user to input a rank number
3. returns the person who has the given rank
"""

rankings = ['John', 'Sen', 'Lisa']
user_input = int(input("Please enter a ranking number 1 to 3: "))
user_input = user_input - 1
print(rankings[user_input])

"""
Coding Exercise 3
rankings = ['John', 'Sen', 'Lisa']
1. contains rankings list
2. prompts persons name
3. returns their rank
"""

user_input = input("Enter a persons name (John, Sen, or Lisa): ")
rank = rankings.index(user_input)
rank += 1
print(rank)
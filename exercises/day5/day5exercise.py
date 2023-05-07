#enumerate practice

# enumerated list
a = enumerate(["a", "b", "c"])

# printing the enumerated list
print(a)
# prints memory location of enumerated object

# printing the enumerated list as a list 
print(list(a))
# prints a list of the enumerated list as tuples nested in a list.


# waiting list

waiting_list = ["Sen", "ben", "john"]

for index, item in enumerate(waiting_list):
    print(f"{index + 1}.{item.title()}")


# exercise 1
filenames = ['document', 'report', 'presentation']
#print out enumerated list of filenames
for i, j in enumerate(filenames):
    print(f"{i}-{j.capitalize()}")

# exercise 2
ips = ['100.122.133.105', '100.122.133.111']
# prompt user to input index ( 0 or 1 )
# return the ip of that index
ip_index = input("enter an index: ( 0 or 1 ) ")
print(f"{ips[int(ip_index)]}")
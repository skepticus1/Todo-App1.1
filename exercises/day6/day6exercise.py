# examples bonus

# make files from filenames and add strings from contents
contents = ["All carronts are to be slice long ways",
    "The carronts were reportedly sliced", 
    "The carrots were confirmed to be sliced"]
filenames = ["doc.txt", "report.txt", "presentation.txt"]


for content, filename in zip(contents, filenames):
    file = open(f"app1/exercises/files/{filename}", 'w')
    print(f"writing {content} to {filename}")
    file.write(content)
    file.close()


#exercise 1
file = open(f"app1/exercises/files/essay.txt", "r")
essay = file.read()
print(essay.title())
file.close()

#exercise 2
file = open(f"app1/exercises/files/essay.txt", "r")
essay = file.read()
print(len(essay))

#exercise 3
member = input(f"Please add a new member: ")

file = open(f"app1/exercises/files/members.txt", "r")
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open(f"app1/exercises/files/members.txt", "w")
file.writelines(existing_members)
file.close()

#exercise 4
bottles = ['1', '2', '3']

for bottle in bottles:
    file = open(f"app1/exercises/files/temp/{bottle}", 'w')
    file.write('hello')
    file.close()

#exercise 5
files = ['a', 'b', 'c']
for f in files:
    file = open(f"app1/exercises/files/{f}.txt", 'r')
    a = file.read()
    print(a)
    file.close()
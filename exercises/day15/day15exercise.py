import glob
import csv
import shutil
import webbrowser

#
# glob example
#
myfiles = glob.glob("*.txt")
print(myfiles)

myfiles = glob.glob("app1/exercises/files/*.txt")
for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())

#
# csv example
#
with open("app1/exercises/files/weather.csv") as file:
    data = list(csv.reader(file))

print(data)

for row in data:
    print(row)

city = input("Enter a city: ")

for row in data:
    if row[0] == city:
        print(row[1])

#
# shutil (shell utilities)
#
shutil.make_archive("output", "zip", "app1/exercises/files")

#
# webbrowser
#
user_term = input("Enter a search term: ")

webbrowser.open("https://google.com/search?q=" + user_term)
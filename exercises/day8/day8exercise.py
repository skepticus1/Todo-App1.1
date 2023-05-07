with open("app1/exercises/files/day8.txt", "r") as file:
    new_file = file.read()
    print(file.read()) #nothing here, empty string

print(new_file)


# 1
# coin flip probability program
# program asks for heads or tails
# user flips coin on desk
# loops
# each loop program prints percentage of heads
# write each result into a file with-context manager

cnt = 0
head = 0

while True:
    with open("app1/exercises/files/day8coin.txt") as file:
        save = file.readlines()
    result = input("Throw the coin and enter head or tail here: ")
    cnt += 1

    if result == "head":
        head += 1
        percent = (head / cnt) * 100
        to_write = f"Result was {result} percentage heads is {percent} % \n"
        save.append(to_write)
        with open("app1/exercises/files/day8coin.txt", "w") as file:
            file.writelines(save)
    
    elif result == "tail":
        percent = (head / cnt) * 100
        to_write = f"Result was {result} percentage heads is {percent} % \n"
        save.append(to_write)
        with open("app1/exercises/files/day8coin.txt", "w") as file:
            file.writelines(save)
    print(percent, "%")
    

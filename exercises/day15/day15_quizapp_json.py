import json

with open("exercises/day15/files/questions.json", 'r') as file:
    content = file.read()

#print(type(content))
#print(content)

data = json.loads(content)
#print(type(data))
#print(data)

score = 0
for question in data:
    print(question["questions_text"])
    for index, alt in enumerate(question["alternatives"]):
        print(index + 1, " - ", alt)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


# print(data)

num_correct = 0
num_total = 0
for question in data:
    #print(question['user_choice'], question['correct_answer'])
    if question['user_choice'] == question['correct_answer']:
        num_correct += 1
    num_total += 1
print(f"num_correct = {num_correct} num_total = {num_total}")
print(num_correct/num_total * 100, "%")
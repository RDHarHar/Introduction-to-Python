# Question 1

empDir = {"001": "Tony", "002": "Natasha", "003": "Clint", "004": "Carol", "005": "Bruce"}

for ID, Name in empDir.items():
    print("The employee ID is", ID, "and their name is",Name)

# Question 2

empDirTwo = {"001": ["Tony", "Iron Man", "2008-05-02"], "002": ["Natasha", "Black Widow", "2021-07-09"], "003": ["Clint", "Hawkeye", "2021-11-24"], "004": ["Carol", "Captain Marvel", "2019-03-08"], "005": ["Bruce", "Hulk", "2008-06-13"]}

for employee in empDirTwo:
    for element in empDirTwo[employee]:
        print(f"{employee} - {element}")

# Question 3

empDirThree = {"001": {"Name": "Tony", "Title": "Iron Man", "Start Date": "2008-05-02"}, "002": {"Name": "Natasha", "Title": "Black Widow", "Start Date": "2021-07-09"}, "003": {"Name": "Clint", "Title": "Hawkeye", "Start Date": "2021-11-24"}, "004": {"Name": "Carol", "Title": "Captain Marvel", "Start Date": "2019-03-08"}, "005": {"Name": "Bruce", "Title": "Hulk", "Start Date": "2008-06-13"}}

for employee in empDirTwo:
    for element in empDirTwo[employee]:
        print(f"{employee} - {element}")

# Question 4

# A tuple is a list that cannot be modified once it is created. A list can be.

# Question 5

listEmpt = []
tupEmpt = ()
setEmpt = {}

print(listEmpt == tupEmpt)
print(listEmpt == setEmpt)
print(tupEmpt == setEmpt)

# Question 6

# You could use a set to determine if a color had been used multiple times since a Set removes all duplicates. If you check the length of the input after converting it to a set and notice it's smaller than expected, the user entered in multiple of the same entry.

# Question 7

# JSON is a methodology for sending information via an easily readable format for other programs to grab and convert it to a useable data set for the user.
# Python is able to load and dump JSON using 'import json'

# Questeion 8

userInput = input("Enter in 4 letters without having any duplicates: ")

setUserInput = set(userInput)

if len(setUserInput) < 4:
    print("You entered a duplicate you fool!")
elif len(setUserInput) > 4:
    print("You entered in too many numbers you fool!")
else:
    print("Congrats!")

# Question 9

import json

foodDictionary = {"fruit": "apple", "veggie": "lettuce", "meat": "ham"}

jsonString = json.dumps(foodDictionary)
jsonString = jsonString.upper()

loudDictionary = json.loads(jsonString)

print(loudDictionary)
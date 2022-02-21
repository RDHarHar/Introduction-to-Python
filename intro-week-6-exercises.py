# Question 1

listVal = [1, 2, 3, 4, 5]

num = 0

while num < len(listVal):
    print(listVal[num])
    num = num + 1

# Question 2

while True:
    value = int(input("Enter in a number between 100 and 200: "))
    if value < 100 or value > 200:
        print("Error, value must be between 100 and 200, please try again")
    else:
        print(value**2)
        break

# Question 3

validInput = False

while validInput == False:
    value = int(input("Enter in a number between 100 and 200: "))
    if value < 100 or value > 200:
        print("Error, value must be between 100 and 200, please try again")
    else:
        print(value**2)
        validInput = True

# Question 4

listOne = [1, 2, 3, 4, 5]
listTwo = [6, 7, 8, 9, 10]

num = 0

while num < len(listTwo):
    listOne.append(listTwo[num])
    num = num+1

print(listOne)

# Question 5

revList = [1, 2, 3, 4, 5]
newList = []

num = 4

while num > -1:
    newList.append(revList[num])
    num = num - 1

print(newList)

# Question 6

finished = False
newList = []

while finished == False:
    num = input("Please enter in a number or 'done' if you are finished: ")
    if num.isdigit():
        newList.append(int(num))
    elif num == "done":
        finished = True
    else:
        print("Error: Please enter in a valid input")

print(newList)
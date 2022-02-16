# Question 1

# The keyword 'in' is useful for checking if something is in a list without using a loop to check each element individually

# Question 2

# That gives an error because you aren't defining 12345 as anything. It would need to be [1, 2, 3, 4, 5]

# Question 3

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(arr)):
    newVal = arr[i] - 1
    print(newVal)
    print(newVal in arr)

# Question 4

x = 8

y = x*2 if x%2 == 0 else x*3

print(y)

# Question 5

userInput = input("Please enter a string: ")

if ' ' in userInput:
    userInput = "Invalid Input"
    print (userInput)
else:
    print(userInput)

# Question 6

if len(arr) % 2 == 0:
    for i in arr:
        print(i)
else:
    print(arr[0])

for i in arr if len(arr) % 2 == 0 else arr[:1]:
    print(i)

# Question 7

userInput = input("Please enter your favorite season: ")

print(userInput)

if userInput == "spring":
    print("I love Spring")
elif userInput == "fall":
    print("Apple Cider, yum")
elif userInput == "winter":
    print("Do you want to build a snowman?")
else:
    print("It's nearly over!")

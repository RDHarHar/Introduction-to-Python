# Question 1
from sqlalchemy import true


print("Question 1")

boolOne = "123"
boolTwo = 123

print(boolOne == boolTwo)

# ~~~

# Question 2
print("Question 2")

boolThree = "ABCDEFG"
boolFour = "abcdefg"

print(boolThree == boolFour)

# ~~~

# Question 3
print("Question 3")

boolEmpty = [ ]
boolFull = [1, 2, 3, 4, 5]

print(boolEmpty == boolFull)
print(boolEmpty < boolFull)
print(boolEmpty > boolFull)

# ~~~

# Question 4
print("Question 4")

print("?" < "A")
print("?" > "A")
print("A" > "Z")
print("Z" > "A")

# ~~~

# Question 5
print("Question 5")

boolFive = 2**32
boolSix = 32**2

print(boolFive)
print(boolSix)
print(boolFive > boolSix)

# ~~~

# Question 6
print("Question 6")

print(True > False)
print(False > True)

# ~~~

# Question 7
print("Question 7")

boolSeven = "This is a Test of Capitalized Letters!"
boolEight = ""
checkBool = 0

for i in range(len(boolSeven)):
    if boolSeven[i] >= "A" and boolSeven[i] <= "Z":
        boolEight = boolEight + boolSeven[i]
        checkBool = 1

if checkBool == 0:
    print("Letter ok!")
else:
    print(boolEight)
    
# ~~~

# Question 8
print("Question 8")

checkNum = 123

if checkNum > 100 and checkNum % 3 == 0:
    print("Hooray!")
else:
    print("Oh no!")

# ~~~

# Question 9
print("Question 9")

checkNumTwo = 200

if checkNumTwo % 2 == 0 or checkNumTwo < 0:
    print(checkNumTwo)
else:
    print("Error 1: Number not even or negative")

# ~~~

# Question 10
print("Question 10")

checkLength = [1, 2, 3, 4]

if len(checkLength) % 2 == 0:
    print("The lists length is even")
else:
    print("The lists length is odd")

# ~~~

# Question 11
print("Question 11")

listCheck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if len(listCheck) <= 9:
    for i in listCheck:
        print(i**2)
elif len(listCheck) > 9:
    for i in listCheck[8:]:
        print(i**3)

# ~~~

# Question 12
print("Question 12")

userName = input("Please enter your name: ")
userName = userName.capitalize()

print(f"Hello {userName}, welcome to my program!")

# ~~~

# Question 13
print("Question 13")

numOne = input("Please enter the first number: ")
numTwo = input("Please enter the second number: ")

if numOne > numTwo:
    print(f"Your first number, {numOne}, is bigger")
elif numOne < numTwo:
    print(f"Your second number, {numTwo}, is bigger")
elif numOne == numTwo:
    print(f"You entered the same number!")

# ~~~

# Question 14
print("Question 14")

testInputEnter = input("Do not enter anything here, just hit enter...")

print(testInputEnter)

# ~~~

# Question 15
print("Question 15")

checkBoolInput = input("Type True and hit enter: ")

print(type(checkBoolInput))

# ~~~

# Question 16
print("Question 16")

passNum = 0
userPassword = input("Please enter in a password (no numbers): ")

for i in userPassword:
    if i.isdigit():
        passNum = 1

if passNum == 1:
    print("I said no numbers!")
else:
    print("Password accepted.")
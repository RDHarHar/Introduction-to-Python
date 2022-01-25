# Question 1

empty = []

print(len(empty))

# Question 2

names = ["Turk", "Carla", "Cox"]

print(names[-1])
print(names[-2])

# Question 3 & 4

numList = [1, 2, 3]
numListNew = numList + [4, 5, 6]

print(numList)
print(numListNew)

numListNew.reverse()

print(numListNew)

# Question 5 & 6 & 7 & 8

names.sort()
print(names)

stringPunct = [".", ",", "A", "B", "a", "b"]
stringPunct.sort()

print(stringPunct)

# Question 9

namesEmpty = names + empty

print(namesEmpty)

# Question 10

emptyNums = empty + [1, 2, 3]

print(emptyNums)

# Question 11

stringPunct.pop(-1)

print(stringPunct)

# Question 12

del stringPunct[-1]

print(stringPunct)

# Question 13

string = "Hello, my name is JD"

string.replace("JD", " ")

print(string)

# Question 14

newString = string.lower() + string.upper()

print(newString)

# Question 15

emptString = ""

emptLow = emptString.lower()
print(emptLow)

emptUp = emptString.upper()
print(emptUp)

emptTitle = emptString.title()
print(emptTitle)

emptCap = emptString.capitalize()
print(emptCap)

# Question 16

words = ["Audio", "Meats", "Knoll"]

wordOneUp = words[0].upper()
wordOneLow = words[0].lower()

wordTwoUp = words[1].upper()
wordTwoLow = words[1].lower()

wordThreeUp = words[2].upper()
wordThreeLow = words[2].lower()

print(wordOneUp)
print(wordOneLow)
print(wordTwoUp)
print(wordTwoLow)
print(wordThreeUp)
print(wordThreeLow)
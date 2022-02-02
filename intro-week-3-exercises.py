# Question 1

listOne = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
j = 0

for i in listOne:
    listSqrd = i * i
    print(f"Index: {j}")
    print(f"Number: {i}")
    print(f"Squared: {listSqrd}")
    j = j + 1

#~~~

# Question 2

listTwo = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for i in range(len(listTwo)):
    listSqrd = listTwo[i] * listTwo[i]
    print(f"Index: {i}")
    print(f"Number: {listTwo[i]}")
    print(f"Squared: {listSqrd}")

#~~~

# Question 3

listThree = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for index, i in enumerate(listThree):
    listSqrd = i * i
    print(f"at index {index} we have value {i} and when squared is {listSqrd}")

#~~~

# Question 4

for value in range(4):
    print(value)

for value in range(-4):
    print(value)

#~~~

# Question 5

listFour = []

for i in listFour:
    print(i)

#~~~

# Question 6

listFive = ["JFK", "Loncoln", "Washington", "Taft", "Jefferson", "Hamilton"]

print(listFive[:5])

#~~~

# Question 7

print(listFive[0:1] + listFive[3:6])

#~~~

# Question 8

print(listFive[:10])

#~~~

# Question 9

print(listFive[-1:])
print(listFive[-2:])

#~~~

# Question 10

print(listFive[:-1])
print(listFive[:-2])

#~~~

# Question 11

print(listFive[4:3])

#~~~

# Question 12

name = "Ryan Douglas Harwick"

print(name[:4])
print(name[5:12])
print(name[13:20])

#~~~

# Question 13

listSix = ["Juan", "Todd", "Sylvia", "Erica", "Abe", "Cal", "Ryan", "Izze", "Steve", "Tony"]

for i in listSix[:5]:
    print(i.upper())

for i in listSix[5:]:
    print(i.lower())

#~~~

# Question 14

listSeven = list(range(1000))
print(min(listSeven))
print(max(listSeven))
# Question 1

def checkForSpace(userString):
    valid = 0
    while valid == 0:
        if " " in userString:
            print("Do not enter in any spaces, try agrain.")
        elif " " not in userString:
            userString = userString.upper()
            valid = 1

    return userString

userString = input("Please enter in ary string with no spaces: ")
checkForSpace(userString)

# Question 2

def userFullName():
    userFirst = input("Please enter your first name with no spaces: ")
    userFirstUpper = checkForSpace(userFirst)

    userSecond = input("Please enter your last name with no spaces: ")
    userSecondUpper = checkForSpace(userSecond)

    return(userFirstUpper, userSecondUpper)

userFirst, userSecond = userFullName()

print(f"Your name is ", userFirst, " ", userSecond)

# Question 3

def print_year(d, m, year="2022"):
    if m == "1":
        month = "January"
    elif m == "2":
        month = "February"
    elif m == "3":
        month = "March"
    elif m == "4":
        month = "April"
    elif m == "5":
        month = "May"
    elif m == "6":
        month = "June"
    elif m == "7":
        month = "July"
    elif m == "8":
        month = "August"
    elif m == "9":
        month = "September"
    elif m == "10":
        month = "October"
    elif m == "11":
        month = "November"
    elif m == "12":
        month = "December"
    else:
        print ("Invalid input")

    print(f"You have selected", month, d, year)

d = input ("Please enter in the number for what day you want to use: ")
m = input("Please enter in the number for what month you want to use: ")
y = input("Please etner in the number for what year you want to use (optional): ")

print_year(d, m, y)

# Question 4


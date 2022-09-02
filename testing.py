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
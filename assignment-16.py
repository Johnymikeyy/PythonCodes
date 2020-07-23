#Find out if a given year is a "leap" year.

year = int(input("Please enter the year which yot want to learnt whether it is leap year\n"))
check = False

if year % 100 == 0 and year % 400 == 0:
    check = True
elif year % 4 == 0:
    check = True

print ("{} is a leap year".format(year)) if check == True else print ("{} is a not leap year".format(year))
yearAge = int(input("Enter the year/age\n"))

isAge = 0
isYear  = 0
count = 0
if yearAge<125 and yearAge >0:
    isAge = 2021 - yearAge
    print(f"In the year of {isAge + 100} your age is 100 years")

elif (yearAge>=1900 and yearAge<=2021) or len(str(yearAge)) == 4:
    isYear = yearAge + 100
    print(f"In the year {isYear} your age is 100 years")

elif yearAge<1900:
    print("You are too old bro, I salute you")

elif yearAge>2021:
    print("You are not born yet LOL")

else:
    print("There is a problem in you input")

interestedYear = int(input("Enter the specific year in which you want to know your age\n"))

for i in range(yearAge, interestedYear+1):
    count = count + 1

print(f"In the year of {interestedYear} you age is {yearAge + count}")
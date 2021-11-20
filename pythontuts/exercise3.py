n = 18

no_of_Guesses = 1

while(no_of_Guesses<=9):
    a = int(input("Enter the number:\n"))
    if a<n:
        print("You guessed to low! Increase your number")
        print("No of guesses left ", 9-no_of_Guesses)
        no_of_Guesses = no_of_Guesses + 1
        continue
    elif a>n:
        print("You guessed to high! Decrease your number")
        print("No of guesses left ", 9 - no_of_Guesses)
        no_of_Guesses = no_of_Guesses + 1
        continue
    else:
        print("Congrates You guessed the number 18")
        print("You Guessed the number at ", no_of_Guesses , "chance")
        break

if no_of_Guesses > 9:
    print("Sorry you take Your all chances! None of Your chances left")

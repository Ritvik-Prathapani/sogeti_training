import random
def main():
    print("Welcome to number guessing game you have to guess a number between 1 and 100 \"only 3 tries are allowed\"")
    number=random.randint(1,100) # This is the number that the user has to guess
    number_of_guesses=3
    while(number_of_guesses):
        guess=int(input("Enter your guess: "))
        if(guess==number):
            print("Congratulations! You guessed the number") 
            break
        elif(guess>number):
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        number_of_guesses-=1
    if(number_of_guesses==0):   # This is the condition when the user has used all the guesses
        print(f"the number was {number}")
main() # This is the function that runs the game
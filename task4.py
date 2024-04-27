import random


def decide_winner(userchoice, compchoice):
    if userchoice == compchoice:
        return "It's a Tie!"
    elif (userchoice == 'rock' and compchoice == 'scissors') or \
            (userchoice == 'scissors' and compchoice == 'paper') or \
            (userchoice == 'paper' and compchoice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"


def main():
    userscore = 0
    compscore = 0

    print("Rock, Paper, Scissors!")

    while True:
        print("\nChoose: rock, paper, or scissors.")
        userchoice = input("Your choice: ").lower()

        if userchoice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        compchoice = random.choice(['rock', 'paper', 'scissors'])

        print(f"\nYour choice: {userchoice}")
        print(f"Computer's choice: {compchoice}")

        result = decide_winner(userchoice, compchoice)
        print(result)

        if result == "You win!":
            userscore += 1
        elif result == "Computer wins!":
            compscore += 1

        print(f"\nScore - You: {userscore}  Computer: {compscore}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Well Played")
            break


if __name__ == "__main__":
    main()

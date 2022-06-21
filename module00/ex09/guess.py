import random
FAILED = -1
SUCCESS = 0


def print_rules() -> None:
    print("==================================================")
    print("This is an interactive guessing game!")
    print("You have to find out the secret number.")
    print("To do so please enter a number between 1 and 99.")
    print("Type 'exit' to end the game. Good luck!")
    print("==================================================")


def check_usr_input(guess:  int) -> int:
    """ This function """
    try:
        guess = int(guess)
    except ValueError:
        if guess == 'exit':
            print("Goodbye!")
            quit()
        else:
            print("That's not a number.\n")
            return FAILED
    return SUCCESS


def check_win_event() -> int:
    if guess == number:
        win_print()
        return SUCCESS
    elif guess > number:
        print("Too high!\nTry again!\n")
    elif guess < number:
        print("Too low!\nTry again!\n")


def win_print() -> None:
    if number == 42:
        print("The answer to the ultimate question of life", end='')
        print("the universe and everything is 42.")
    if n_try == 1:
        print("Congratulations! You won the game on your first try!")
    else:
        print("Congratulations! You won the game in", n_try, "attempts!")


if __name__ == "__main__":
    number = random.randint(1, 99)
    guess = 0
    n_try = 0

    while True:
        n_try += 1
        print_rules()
        guess = input(">> ")
        if check_usr_input(guess) == FAILED:
            continue
        else:
            guess = int(guess)
            if check_win_event() == SUCCESS:
                quit()

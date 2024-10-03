import random


def compare_number(goal_number, your_number):
    """
    Compare the goal number with the number that user guessed

    Args:
        goal_number (int): The goal number that was generated randomly
        your_number (int): The number that was inputed by user

    Return:
        boolean: If is the right answer then True, else will be false
    """
    if your_number == goal_number:
        print(f"The goal_number is {goal_number}.")
        return True
    elif your_number < goal_number:
        print("Too low, try it again!")
        return False
    else:
        print("Too high, try it agein!")
        return False


def play_game(times):
    """
    The main logic function

    Args:
        times (int): the times that user can play
    """
    goal_number = random.randint(1, 100)
    # This line is just for debug
    # print(goal_number)

    for time in range(times):
        your_number = int(input("Choose your number (1~100):"))
        result = compare_number(goal_number, your_number)
        if result is True:
            print("You win!")
            break


def main():
    next_game = "y"
    times = {"hard": 5, "easy": 10}

    while next_game == "y":
        choose_hard = input(
            "Choose difficulty game version? type easy or hard:\n"
        )
        play_game(times[choose_hard])
        next_game = input("Do you want a new game? type y or n :\n")
    else:
        print("good bye~")
        next_game = "n"


main()

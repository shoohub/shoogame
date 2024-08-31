import random

# 比較する
def game(goal_number, your_number):
    if your_number == goal_number:
        print(f"the goal_number is {goal_number}")
        return True
    elif your_number < goal_number:
        print("too low")
        return False
    else:
        print("too high")
        return False


def play_game(times):
    """
    xxxxxxx

    Args:
        time (int): xxxxx

    return
        bool: xxxxx  
    """
    goal_number = random.randint(1,100)
    print(goal_number)

    for time in range(times):
        your_number = int(input("choose your number :"))
        result = game(goal_number,your_number)
        if result is True:
            print("you win.")
            break


def main():
    next_game = "y"
    #モードを選ぶ
   
    times = {"hard":5,"easy":10}
    
    while next_game == "y":
        choose_hard = input("choose difficulty of game you want? type easy or hard:\n")
        play_game(times[choose_hard])
        next_game = input("do you want a new game?type y or n :\n")
    else:
        print("good bye~")
        next_game = "n"

main()
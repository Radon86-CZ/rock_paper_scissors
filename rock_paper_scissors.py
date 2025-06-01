import random

player_wins = 0
pc_wins = 0
ties = 0
options = ["rock", "paper", "scissors"]


while True:
    player_pick = input("Type rock / paper / scissors to play, or 'Q' to quit: ").lower()

    if player_pick == "q":
        break

    if player_pick not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    pc_pick = options[random_number]

    print("PC picked " + str(pc_pick) + ".")

    if player_pick == "rock" and pc_pick == "scissors":
        print("You won!")
        player_wins +=1

    elif player_pick == "paper" and pc_pick == "rock":
        print("You won!")
        player_wins +=1

    elif player_pick == "scissors" and pc_pick == "paper":
        print("You won!")
        player_wins +=1

    elif player_pick == "rock" and pc_pick == "rock":
        print("Tie!")
        ties += 1

    elif player_pick == "paper" and pc_pick == "paper":
        print("Tie!")
        ties += 1

    elif player_pick == "scissors" and pc_pick == "scissors":
        print("Tie!")
        ties +=1

    else:
        print("You lost!")
        pc_wins +=1

print("You won " + str(player_wins) + " times, tied " + str(ties) + " times and lost " + str(pc_wins) + " times.")
print("Bye!")
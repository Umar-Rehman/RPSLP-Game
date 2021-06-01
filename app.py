# GAME RULES:

# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# (and as it always has) Rock crushes Scissors


class Rules():
    Rule1 = '- Scissors cuts Paper'
    Rule2 = '- Paper covers Rock'
    Rule3 = '- Spock smashes Scissors'
    Rule4 = '- Scissors decapitates Lizard'
    Rule5 = '- Lizard eats Paper'
    Rule6 = '- Paper disproves Spock'
    Rule7 = '- Spock vaporizes Rock'
    Rule8 = '- (and as it always has) Rock crushes Scissors'


print(
    f"First time playing Rock Paper Scissors Lizard Spock? How does it work, you ask?\n\nOh it's very simple:\n\n{Rules.Rule1}\n{Rules.Rule2}\n{Rules.Rule3}\n{Rules.Rule4}\n{Rules.Rule5}\n{Rules.Rule6}\n{Rules.Rule7}\n{Rules.Rule8}\n\nLet's begin..."
)
import random
from enum import IntEnum


# Defines a class with values assigned to each choice
class Choice(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3
    Lizard = 4
    Spock = 5


# Defines the win conditions in an object
win_condition = {
    Choice.Scissors: [Choice.Lizard, Choice.Paper],
    Choice.Paper: [Choice.Spock, Choice.Rock],
    Choice.Rock: [Choice.Lizard, Choice.Scissors],
    Choice.Lizard: [Choice.Spock, Choice.Paper],
    Choice.Spock: [Choice.Scissors, Choice.Rock]
}


# Gets users choice
def user_choice():
    choices = [f"{action.name}[{action.value}]" for action in Choice]
    choices_str = ", ".join(choices)
    selection = int(input(f"\nMake your choice ({choices_str}): "))
    action = Choice(selection)
    return action


# Randomizes computers choice
def comp_choice():
    selection = random.randint(1, len(Choice))
    action = Choice(selection)
    return action


# Finds the winner of the round
def who_wins(user_action, comp_action):
    if user_action == comp_action:
        print(f"\nWe both picked {user_action.name}. It's a tie!\n")

    # All possible outcomes if user picks ROCK
    # print(f"You chose {user_action.name} and I chose {comp_action.name}, and everyone knows that... ")
    if user_action == Choice.Rock:

        if comp_action == Choice.Scissors:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Rock smashes Scissors!\n\nSo I guess you win this time...\n"
            )
        elif comp_action == Choice.Lizard:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Rock crushes Lizard!\n\nSo I guess you win this time...\n"
            )
        elif comp_action == Choice.Paper:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Paper covers Rock! \n\nYou lose! I'll go easy on you next time...\n"
            )
        elif comp_action == Choice.Spock:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Spock vaporizes Rock! \n\nYou lose! I'll go easy on you next time...\n"
            )

    # All possible outcomes if user picks PAPER
    elif user_action == Choice.Paper:

        if comp_action == Choice.Rock:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Paper covers Rock!\n\nSo I guess you win this time...\n"
            )
        elif comp_action == Choice.Spock:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Paper disproves Spock!\n\nSo I guess you win this time...\n"
            )
        elif comp_action == Choice.Scissors:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Scissors cuts Paper! \n\nYou lose! I'll go easy on you next time...\n"
            )
        elif comp_action == Choice.Lizard:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Lizard eats Paper! \n\nYou lose! I'll go easy on you next time...\n"
            )

    # All possible outcomes if user picks SCISSORS
    elif user_action == Choice.Scissors:

        if comp_action == Choice.Paper:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Scissors cuts paper!\n\nSo I guess you win this time...\n"
            )
        elif comp_action == Choice.Lizard:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Scissors decapitates Lizard!\n\nSo I guess you win this time...\n"
            )
        elif comp_action == Choice.Rock:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Rock smashes scissors! \n\nYou lose! I'll go easy on you next time...\n"
            )
        elif comp_action == Choice.Spock:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Spock smashes Scissors! \n\nYou lose! I'll go easy on you next time...\n"
            )

    # All possible outcomes if user picks LIZARD
    elif user_action == Choice.Lizard:

        if comp_action == Choice.Paper:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Lizard eats paper!\n\nSo I guess you win this time...\n"
            )
        elif comp_action == Choice.Spock:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Lizard poisons Spock!\n\nSo I guess you win this time...\n"
            )
        elif comp_action == Choice.Rock:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Rock crushes Lizard! \n\nYou lose! I'll go easy on you next time...\n"
            )
        elif comp_action == Choice.Scissors:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Scissors decapitates Lizard! \n\nYou lose! I'll go easy on you next time...\n"
            )

    # All possible outcomes if user picks SPOCK
    elif user_action == Choice.Spock:

        if comp_action == Choice.Scissors:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Spock smashes Scissors!\n\nSo I guess you win this time...\n"
            )
        elif comp_action == Choice.Rock:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Spock vaporizes Rock!\n\nSo I guess you win this time...\n"
            )
        elif comp_action == Choice.Paper:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Paper disproves Spock! \n\nYou lose! I'll go easy on you next time...\n"
            )
        elif comp_action == Choice.Lizard:
            print(
                f"\nYou chose {user_action.name} and I chose {comp_action.name}, and everyone knows that Lizard poisons Spock! \n\nYou lose! I'll go easy on you next time...\n"
            )


# Validates choice input to be within the range of the options available in the class Choice. Calls the main functions to get user choice, comp choice and compares them to find a winner. Includes a 'Play again?' loop.
while True:
    try:
        user_action = user_choice()
    except ValueError:
        range_str = f"[1, {len(Choice)}]"
        print(f"\nInvalid selection. Enter a value in range {range_str}\n")
        continue

    comp_action = comp_choice()
    who_wins(user_action, comp_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

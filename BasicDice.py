import random
roll_again = "yes"
guess1 = 0
guess2 = 0
die1 = 0
die2 = 0
final_guess = (guess1 , guess2)
final_guessinv = (guess2 , guess1)
final_die = (die1 , die2)
bet = 0
winnings = 0
final_winnings = 0
print ("Welcome to dice-o-rama! Guess the dice and win some cash!\n")
print ("Rules:\n $1 to play\n If you guess any die, you win $1\n If you guess a pair, you win $20\n Wanna play (yes or no)?\n")
roll_again = input(str)
if roll_again == "yes" or roll_again == "y":
    print ("Let's see how you roll!")
    bet = (bet - 1)
else:
        print ("Then quit wasting my time!")
while roll_again == "yes" or roll_again == "y":
    print ("Please guess the first die:\n")
    guess1 = input(int)
    if int(guess1) < 1 or int(guess1) > 6:
        print ("Wow! Do you know how dice work?\n")
    print ("Please guess the second die:\n")
    guess2 = input(int)
    if int(guess2) < 1 or int(guess2) >6:
        print ("... dude ... what?\n")
    final_guess = (guess1 , guess2)
    final_guessinv = (guess2 , guess1)
    print ("Here's your guess:" + str(final_guess))
    if int(guess1) < 1 or int(guess1) > 6 and int(guess2) < 1 or int(guess2) >6:
        print ("That was hard to watch")
    elif int(guess1) < 1 or int(guess1) > 6 or int(guess2) < 1 or int(guess2) >6:
        print ("You still got a shot, Chief!")
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    final_die = (die1 , die2)
    print ("\nThe Results!" + str(final_die))
    if [int(guess1) , int(guess2)] == [int(die1) , int(die2)] or [int(guess2) , int(guess1)] == [int(die1) , int(die2)]:
        bet = (bet + 1)
        winnings = (bet + 20)
        final_winnings = (final_winnings + winnings)
        print ("\n Wow! That's ten bucks to you, Partner!")
    elif int(guess1) == int(die1) or int(guess1) == int(die2) or int(guess2) == int(die1) or int(guess2) == int(die2):
        bet = (bet + 1)
        winnings = (bet + 1)
        final_winnings = (final_winnings + winnings)
        print ("\nCongratdulations, you won a buck!")
    else:
        print ("\nAh! Better luck next time...")
        winnings = (winnings - 1)
        final_winnings = (final_winnings + winnings)
    bet = 0
    winnings = 0
    print ("Your Total Winnings:" + str(final_winnings))
    roll_again = input("Roll the dice again?\n")
    if roll_again == "yes" or roll_again == "y":
        bet = bet - 1
        print ("Let's keep em rollin'")
if roll_again != "yes" or roll_again != "y":
    print ("Final Winnings:" + str(final_winnings))
    print ("Safe travels, Partner...")

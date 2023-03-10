import random

def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    return random.choice(["rock","paper","scissors"])
    

def rps(player1, player2):
    """
    input: player1, play2 --> "rock","paper", or "scissors."
    output: "player1 win!", "player2 win!", or "It's a tie!"
    """
    #it's a tie
    if player1 == player2:
      print("It's a tie!")

    #player1= rock
    elif player1 == "rock":
      if   player2 == "paper": 
        print("player2 win!")
      elif player2 == "sciccors":
        print("player1 win!")

    #player = paper
    elif player1 == "paper":
      if player2 == "rock":
        print("player1 win!")
      elif player2 == "scissors":
        print("player1 win!")

    #player1 = "scissors"
    elif player1 == "scissors":
      if player2 =="rock":
        print("player2 win!")
      elif player2 == "paper":
        print("player1 win!")

def play_again():
  user_input = input("Would you like to play it again? Yes or No)")
  if user_input.lower() == "yes":
    return True
  else:
    return False
    #return random.choice([True, False])

def run_game():
  play = True
  while play == True:
    #assign rock, paper, and scissor for player1 and player2
    player1 = choose_rps()
    player2 = choose_rps()


      #output choices for user
    print(f'player 1 chose {player1}')
    print(f'player 2 chose {player2}\n')

      #output the winner
    rps(player1, player2)
    print("\n-----\n")

    play = play_again()

run_game()
print("Thank you for playing!")


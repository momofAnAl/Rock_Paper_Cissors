import rps_function
import random

rps = ['rock', 'paper', 'scissors']

def choose_rps():
  "output: randomly returns rock, paper, or scissors"
  r = random.randint(0,2)
  print(r)
  return rps[r]
  
def play_again():
  "output: 1 or 0 for play again or not"
  r = random.randint(0,1)
  return r

play = True

print("Welcome to Rock, Paper, Scissors!")
print("------")
while play == True:
  player1 = choose_rps()
  player2 = choose_rps()
  print(f"Player 1 chose {player1}")
  print(f"Player 2 chose {player2}\n")
  rps_function.rps(player1, player2)
  play = play_again()
  print("------")

print("Thank you for playing!")

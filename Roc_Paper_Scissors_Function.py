def rps(player1, player2):
  """
  input: player1 and player2 -> 'rock','paper', 'scissors'
  output: "Player 1 wins!", "Player 2 Wins!", "It's a tie!"
  """
  # tie
  if player1 == player2:
    print("It's a tie!")

  # player 1 = rock
  elif player1 == 'rock':
    if player2 == 'paper':
      print("Player 2 wins!")
    elif player2 == 'scissors':
      print("Player 1 wins!")

  # player 1 = paper
  elif player1 == 'paper':
    if player2 == 'rock':
      print("Player 1 wins!")
    elif player2 == 'scissors':
      print("Player 2 wins!")

  # player 1 = scissors
  elif player1 == 'scissors':
    if player2 == 'rock':
      print("Player 2 wins!")
    elif player2 == 'paper':
      print("Player 1 wins!")

rps('rock', 'rock')
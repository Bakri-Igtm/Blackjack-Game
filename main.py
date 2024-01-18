############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
# from replit import clear
from art import logo
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Push!!!"
  elif user_score == 0:
    return "You Win with a Blackjack!!!"
  elif computer_score == 0:
    return "Computer Wins with a Blackjack!!!"
  elif user_score > 21:
    return "You Lose!!!"
  elif computer_score > 21:
    return "Computer Loses!!!"
  elif user_score > computer_score:
    return "You Win!!!"
  else:
    return "You Lose!!!"


def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
  #and returns the score. 
  #Look up the sum() function to help you do this.
  def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
      return 0
    if sum(cards) > 21:
      if 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
  #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  game_over = False
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_deal == "y":
        user_cards.append(deal_card())
      else:
        game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  
  
  #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
  
  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  
  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  
  #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
  
  print(compare(user_score, computer_score))
  print(computer_cards)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  # clear()
  play_game()
  #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
  

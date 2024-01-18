import random
from art import logo
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
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
  def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
      return 0
    if sum(cards) > 21:
      if 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
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
  
  
  
  print(compare(user_score, computer_score))
  print(computer_cards)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
 
  

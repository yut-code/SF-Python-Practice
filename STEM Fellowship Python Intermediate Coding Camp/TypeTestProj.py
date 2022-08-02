#PROJECT: WAR CARD GAME
# import random
import requests

#Randomly pick a card for the user and for the dealer. Whoever's card is higher in value wins the match! If there's a tie, the dealer wins by default. Note that you can ignore suits in this game since we only care about rank.

def randCards():
  response = requests.get('https://www.deckofcardsapi.com/api/deck/new/draw/?count=2')
  data = response.json()
  userCard = data['cards'][0]['value']
  dealer = data['cards'][1]['value']
  return userCard, dealer

def unique(yourCard, dealerCard):
  if yourCard in uniqValues:
    yourCard = uniqValues[yourCard]
  if dealerCard in uniqValues:
    dealerCard = uniqValues[dealerCard]
  return yourCard, dealerCard


uniqValues = {"JACK": 11, "QUEEN": 12, "KING": 13, "ACE": 14}
print('Welcome to the War Card Game!\n')

while True:
  cards = randCards()
  yourCard = cards[0]
  dealerCard = cards[1]
  print('You have:', yourCard)
  print('Dealer has:', dealerCard)
  
  if yourCard == dealerCard:
    print('WAR!\n')
    continue
  
  else:
    if yourCard in uniqValues or dealerCard in uniqValues:
      cards = unique(yourCard, dealerCard)
      yourCard = cards[0]
      dealerCard = cards[1]
    
    W = max(int(yourCard), int(dealerCard))
    
    if W == int(yourCard):
      print('\nYou won!')
    else:
      print('\nYou lost...')
    break
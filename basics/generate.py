import random

coin = random.choice(['heads', 'tails'])

print(coin)

cards = ['king','queen', 'jack']
random.shuffle(cards)

for card in cards:
    print(card)
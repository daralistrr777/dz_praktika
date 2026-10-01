import random

deck = [f'{v}{s}' for s in '♠♥♦♣' for v in '6789TJQKA' ]
random.seed(7)
print('vsego kart v kolode  :', len(deck))

hand = random.sample(deck,5)
print('ruka igroka (sample)  :', hand)

print('karta dnya (choice)  :', random.choice(deck))

weights = {'obichnaya': 70, 'redkaya': 20, 'legendarnaya': 5 }
loot = random.choices(list(weights), weights=list(weights.values()), k=5)
print('lut (choices, 5 sht.):', loot)

random.shuffle(deck)
print('posle shuffle  :', deck[:6], "...")

print('\n--- razdacha 3 igrokam po 5 kart ---')
players = ['alisa', 'boris', 'vera']
pool = deck.copy()
for p in players:
    print(f'{p:6s}: {random.sample(pool,5)}')
for card in hand:
    pool.remove(card)

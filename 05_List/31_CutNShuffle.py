def cutDeck(deck):
    first_half = deck[0:len(deck)//2]
    second_half = deck[len(deck)//2:]
    deck = second_half + first_half
    return deck

def shuffleDeck(deck):
    it_1 = 0
    it_2 = len(deck) // 2
    new_deck = []
    for i in range(len(deck)):
        if i % 2 == 0:
            new_deck.append(deck[it_1])
            it_1 += 1
        else:
            new_deck.append(deck[it_2])
            it_2 += 1
    return new_deck

deck = [e for e in input().split()]

for operation in input():
    if operation == 'C':
        deck = cutDeck(deck)
    elif operation == 'S':
        deck = shuffleDeck(deck)

print(*deck)
